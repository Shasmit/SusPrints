from flask import Blueprint, render_template,redirect,request,url_for,flash
from flask_login import login_user,current_user,logout_user,login_required

views = Blueprint('views', __name__)
@views.route('/')
def landingpage():
    return render_template('LandingPage/landingpage.html')

@views.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.Login'))
    return render_template('home/index.html')

@views.route('/Products')
def Products():
    return render_template('Products/products.html')

@views.route('/Profile')
def Profile():
    return render_template('Profile/profile.html')
