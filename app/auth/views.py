# from flask import *
# from flask_login import login_required,current_user,login_user,logout_user
# from . import auth
# from .forms import RegistrationForm,LoginForm
#
# @auth.route('/register',methods=["GET","POST"])
# def register():
#     form=RegistrationForm()
#     if form.validate_on_submit():
#         username=form.username.data
#         password=form.password.data
#         email=form.email.data
#     return render_template('registration.html',form=form)
