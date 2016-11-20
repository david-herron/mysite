from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators


class ContactForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter a valid email address.")])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [validators.DataRequired("Oops.. no message! Please enter a message.")])
    submit = SubmitField("Send", [validators.DataRequired()])