from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, HiddenField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    title = StringField(label="Title", validators=[
                        DataRequired(), Length(min=0, max=50)])
    content = TextAreaField(label="Content")
    tag_id = HiddenField(label="Tag Id")
    save = SubmitField("Save")


class TagForm(FlaskForm):
    name = StringField(label="Name", validators=[
                       DataRequired(), Length(min=0, max=25)])
    save = SubmitField("Save")


class LoginForm(FlaskForm):
    email = EmailField(
        "E-mail", validators=[DataRequired(), Length(min=0, max=60)])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=0, max=100)])
    save = SubmitField("Login")


class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(0, 100)])
    email = EmailField("E-mail", validators=[DataRequired(), Length(0, 60)])
    password = PasswordField("Password", validators=[Length(8, 100)])
    confirm_password = PasswordField("Confirm Password", validators=[Length(8, 100)])
    create_user = SubmitField("Create")
