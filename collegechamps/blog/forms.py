
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators
from wtforms.fields.core import RadioField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=  [DataRequired()])
    subtitle = StringField('Subtitle',validators=[DataRequired()])
    price = RadioField('Choose plan',choices=[('free','free'),('paid','paid')])
    slug = StringField('Slug',validators=[DataRequired()])
    price = RadioField('Price',choices=[('free','free'),('paid','paid')],validators=[validators.Optional()])
    submit = SubmitField('Post')
    to_redirect = StringField('Redirect Page',validators=[validators.Optional()])
    subject_title = StringField('Subject Title',validators=[validators.Optional()] )