from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField
import sqlalchemy as sa
from app import db
from app.models.user import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        # user = User.query.filter_by(username=username.data).first()
        # or
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        email = db.session.scalar(sa.select(User).where(User.email == email.data))
        if email:
            raise ValidationError('That email is taken. Please choose a different one.')
