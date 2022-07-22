from itertools import product
from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileRequired, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    cpassword = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Login')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    image = FileField('Image',validators=[FileAllowed(["png",'jpg'])])
    price = StringField('Price',validators=[DataRequired()])
    submit = SubmitField('Add Product')
    productType = StringField('Product Type')
    discountPrice = StringField('Discount Price')

class AddCarts(FlaskForm):
    item_id = IntegerField('Item ID',validators=[DataRequired()])
    user_id = IntegerField('user ID',validators=[DataRequired()])
    type = StringField('Type',validators=[DataRequired()])
    submit = SubmitField('Add to Cart')

class DeleteCart(FlaskForm):
    item_id = IntegerField('Item ID',validators=[DataRequired()])
    user_id = IntegerField('user ID',validators=[DataRequired()])
    type = StringField('Type',validators=[DataRequired()])
    submit = SubmitField('Add to Cart')