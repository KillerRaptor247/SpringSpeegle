# forms.py
# Python file for storing the web form of the classes used
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db, app
from app.models import User, Teams


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Username is taken. Please use a different one.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Email is taken. Please use a different one.')


# TODO CREATE FORM CLASS FOR TEAMS AND YEARS
class TeamForm(FlaskForm):
    selectedTeam = SelectField(u'Select Team', validate_choice=False)
    selectedYear = SelectField(u'Select Year', validate_choice=False)
    confirmTeam = SubmitField(u'Confirm Team')
    submitYear = SubmitField(u'Confirm Year')

    # This populates the select field with all of the teams
    def getTeams(self, selectedTeam):
        teams = db.session.execute(db.select(Teams).group_by(Teams.team_name).order_by(Teams.team_name)).scalars()
        selectedTeam.choices = [team.team_name for team in teams]

    def getYears(self, selectedYear, selectedTeam):
        years = db.session.execute(sa.select(Teams).where(Teams.team_name == selectedTeam.data)).scalars()
        selectedYear.choices = [team.yearID for team in years]


class RosterForm(FlaskForm):
    submitFav = SubmitField(u'Favorite?')

    def submitTeam(self, selectedTeam):
        db.session.execute(db.update(User).where(User.username == current_user.username)
                           .values(fav_team=selectedTeam))
        db.session.commit()

    def getLogo(self, selectedTeam):
        logo = db.session.execute(db.select(Teams.team_logo).where(Teams.team_name == selectedTeam)).scalar()
        return logo

    def getBatting(self, selectedTeam, selectedYear):
        battingSQL = ("SELECT CONCAT(nameFirst, ' ', nameLast) as Name, "
                      "G_p, G_c, G_1b, G_2b, G_3b, G_ss, G_lf, G_cf, G_rf, (b_H / b_AB) as batAvg,"
                      " COALESCE(((b_H + b_BB + b_HBP) / (b_AB + b_BB + b_HBP + b_SF)), 0) as basPtg, "
                      "((b_H + b_3B + b_2b) - b_H) + (b_2b * 2) + (b_3b * 3) + (b_hr * 4) / b_AB as slgPtg "
                      "FROM appearances JOIN people USING (playerID) JOIN batting USING(playerID) JOIN teams ON batting.teamID = teams.teamID "
                      "WHERE team_name = :s AND appearances.yearid = :d GROUP BY Name;")
        battingRoster = db.session.execute(sa.text(battingSQL), {"s": selectedTeam, "d": selectedYear})
        return battingRoster.fetchall()

    def getPitching(self, selectedTeam, selectedYear):
        pitchingSQL = ("SELECT CONCAT(nameFirst, ' ', nameLast) as Name, "
                       "G_p, GS, (p_IPOuts / 3) as Inn, "
                       "((p_BB + p_H) / (p_IPOuts / 3)) as WHIP, "
                       "(p_SO / (p_IPOuts / 3)) * 9 as SOp9 "
                       "FROM appearances JOIN pitching USING (playerID) JOIN people USING (playerID) JOIN teams ON pitching.teamID = teams.teamID "
                       "WHERE teams.team_name = :s and appearances.yearID = :d GROUP BY Name;")
        pitchingRoster = db.session.execute(sa.text(pitchingSQL), {"s": selectedTeam, "d": selectedYear})
        return pitchingRoster.fetchall()


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
