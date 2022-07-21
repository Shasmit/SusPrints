from flask import Blueprint, render_template,redirect,request,url_for,flash
from flask_login import login_user,current_user,logout_user,login_required

from models import NewArrivals,MostSelling
import secrets
import os
from __init__ import app

views = Blueprint('views', __name__)
@views.route('/')
def landingpage():
    return render_template('LandingPage/landingpage.html')

@views.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.Login'))
    else:
        newarrival = NewArrivals.query.all()
        mostselling = MostSelling.query.all()
        
        return render_template('home/index.html',newarrival=newarrival,mostselling=mostselling)


def save_pic(pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(pic.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path, "static/Assets/userimage", pic_fn)
    pic.save(pic_path)
    return pic_fn

@views.route('/MostSelling/<string:productname>')
def Products(productname):
    desc = MostSelling.query.filter_by(title=productname).first()
    return render_template('Products/products.html',desc=desc)



@views.route('/NewArrivals/<string:productname>')
def ProductsN(productname):
    desc = NewArrivals.query.filter_by(title=productname).first()
    return render_template('Products/products.html',desc=desc)
      

@views.route('/Profile')
def Profile():
    return render_template('Profile/profile.html')

@views.route('/Cart')
def Cart():
    return render_template('Cart/cart.html')