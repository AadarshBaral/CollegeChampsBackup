from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from collegechamps.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=20, message ='Username is too short!(min-4,max-20)')], render_kw={"placeholder": "Username"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Email Here"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5,max=20,message = 'Too short password!Make it atleast 5 characters long.')], render_kw={
                             "placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password',message ='Passwords did not match!😧')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is already taken😕')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already taken😟')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
                             "placeholder": "Your Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# future account profile implementaiton


# class UpdateAccountForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
#     submit = SubmitField('Update')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
