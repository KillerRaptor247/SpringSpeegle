# forms.py
# Python file for storing the web form of the classes used
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
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
        teams = db.session.execute(db.select(Teams)).scalars()
        selectedTeam.choices = [team.team_name for team in teams]

    def getYears(self, selectedYear, selectedTeam):
        years = db.session.execute(sa.select(Teams).where(Teams.team_name == selectedTeam.data)).scalars()
        selectedYear.choices = [team.yearID for team in years]

class RosterForm(FlaskForm):
        #Do Batting First
    batterName = StringField
