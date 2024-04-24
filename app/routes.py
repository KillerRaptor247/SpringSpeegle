# routes.py
# Contains the routes to the different web pages for the project
from datetime import datetime

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm, TeamForm, RosterForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User, Teams
from urllib.parse import urlsplit


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='CSI 3335 Spring Project')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        app.logger.info('Logging in ' + form.username.data + ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    app.logger.info('Logging out ' + current_user.username + ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        app.logger.info('Registering ' + current_user.username + ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/teamsYears', methods=['GET', 'POST'])
@login_required
def teamsYears():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = TeamForm()
    form.getTeams(form.selectedTeam)
    form.getYears(form.selectedYear, form.selectedTeam)
    if form.validate_on_submit():
        if form.confirmTeam.data:
            flash("YO THE TEAM WAS SUBMITTED")
            app.logger.info(current_user.username + ' has selected ' + form.selectedTeam.data +
                            ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            form.getYears(form.selectedYear, form.selectedTeam)
        elif form.submitYear.data:
            if form.selectedYear.data is not None:
                app.logger.info(current_user.username + ' has selected ' + form.selectedYear.data +
                            ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                flash("Years were submitted. Opening Roster")
                return redirect(url_for('roster', selectedTeam=form.selectedTeam.data, selectedYear=form.selectedYear.data))
    return render_template('teams-years.html', title='Teams-Years', form=form, user=current_user)


@app.route('/roster/<selectedTeam>/<selectedYear>', methods=['GET', 'POST'])
@login_required
def roster(selectedTeam, selectedYear):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RosterForm()
    batting = form.getBatting(selectedTeam, selectedYear)
    pitching = form.getPitching(selectedTeam, selectedYear)
    app.logger.info('Displaying Roster for ' + selectedTeam + ' in ' + selectedYear +
                    ' for user: ' + current_user.username + ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    return render_template('roster.html', title='Roster', form=form, user=current_user,
                           batting_stats=batting,
                           pitching_stats=pitching,
                           teams=selectedTeam, years=selectedYear)


@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    app.logger.info('Displaying Profile for User: ' + username + ' at ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    logfile = open("./logs/adminLog.log", "r")
    lines = logfile.readlines()
    return render_template('user.html', user=user, file=lines)
