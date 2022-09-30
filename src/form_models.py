from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    title = StringField(label="Title", validators=[
                        DataRequired(), Length(min=0, max=50)])
    content = TextAreaField(label="Content")
    save = SubmitField("Save")
