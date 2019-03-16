import flask
from flask import *
from flask_login import login_required
from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile,PostForm
from .. import db,photos
from ..models import *
@main.route('/')
def index():
    posts=Post.query.all()
    number = len(posts)
    title='blog'
    return render_template('index.html',title=title,posts=posts, number=number)

@main.route('/addpost',methods=['GET','POST'])
def add_post():
    form=PostForm()
    if form.validate_on_submit():
        title=form.title.data
        content=form.content.data
        post=Post(title=title,content=content,user_id=current_user.id,date_posted=datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('post.html',form=form)
@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user)
@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form=UpdateProfile()
    if form.validate_on_submit():
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form=form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
