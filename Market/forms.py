from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from Market.models import User


### This class imports from Flask_wtf ('RegisterForm') in the function validate_username it will search for everything with 
# validate_(what ever is here will get validated)

class RegisterForm(FlaskForm):   
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user: 
            raise ValidationError('Username already exists! Pleasee try a different username')
    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
        
    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='email', validators=[Email(), DataRequired()])
    password = PasswordField(label='password', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='confirm_password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='purchase Item')
    
class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')
    