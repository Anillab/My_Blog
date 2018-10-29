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
@main.route('/next/',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password=form.password.data
    return render_template('registration.html',form=form)
@main.route('/love/<username>')
def show(username):
    # return '{}\'s profile'.format(username)
    return f'{username}\'s profile'
# with app.test_request_context():
#     print(url_for('anilla'))
#     print(url_for('carey'))
#     print(url_for('show',username=4))
#
