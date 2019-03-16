from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo
class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us about yourself',validators=[DataRequired()])
    submit=SubmitField('Submit')



class PostForm(FlaskForm):
    title=TextAreaField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    sumit=SubmitField('Post',validators=[DataRequired()])

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment',validators=[DataRequired()])
    submit=SubmitField('SubmitField',validators=[DataRequired()])
