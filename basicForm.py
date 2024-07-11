from flask_wtf import FlaskForm
from wtforms import IntegerField,SelectField, SubmitField

class BasicForm(FlaskForm):
    weight=IntegerField("Weight")
    height=IntegerField("Height")
    unit = SelectField("Unit")
    submit=SubmitField("Submit")
