from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(min=0, max=50)])
    content = TextAreaField(label="Content")
    save = SubmitField("Save")

@dataclass
class Task():
    title: str
    tag: Optional[str]
    content: Optional[str]
    creation_date: datetime
