from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    bio=db.Column(db.String(255))
    profile_pic=db.Column(db.String())
    password_secure=db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.password_secure=generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    content=db.Column(db.Text)
    comments = db.relationship('Comments',backref = 'post',lazy = "dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))


class Subscriber(UserMixin, db.Model):
    __tablename__="subscribers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)

    def save_subscriber(self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def get_subscribers(cls,id):
        return Subscriber.query.all()
