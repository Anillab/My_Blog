import flask
from flask import *
from . import main
from .forms import RegistrationForm
from flask_login import login_required,current_user
@main.route('/')
def anilla():
    message='Hey anilla'
    title='blog'
    return render_template('index.html',message=message,title=title)
@main.route('/next/')
def carey():
    form=RegistrationForm()
    if form.validate_on_submit():
        return render_template('registration.html',form=form)
@main.route('/love/<int:username>')
def show(username):
    # return '{}\'s profile'.format(username)
    return f'{username}\'s profile'
# with app.test_request_context():
#     print(url_for('anilla'))
#     print(url_for('carey'))
#     print(url_for('show',username=4))
#
