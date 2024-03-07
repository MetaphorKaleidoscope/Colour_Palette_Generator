from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired
#  WTForm


class ToolsForm(FlaskForm):
    image = FileField(label='image', validators=[DataRequired()])
    no_colors = IntegerField("Number of colors", validators=[DataRequired()])
    submit = SubmitField(label="RUN!")
