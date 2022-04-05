from random import choices
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

choices=[("Shipped", "Shipped"), ("Resolved", "Resolved"), ("Cancelled", "Cancelled"),
           ("On Hold", "On Hold"), ("Disputed", "Disputed"), ("In Process", "In Process")]


class OrderForm(FlaskForm):
  
    Kosten = DateField("Kosten", [validators.InputRequired()])
    Zielort = DateField("Zielort", [validators.InputRequired()])
    Land = DateField("Land", [validators.InputRequired()])
    Dauer = SelectField("Dauer", choices=choices)
    hotel = TextAreaField("hotel")
    