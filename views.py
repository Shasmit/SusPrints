from flask import Blueprint, render_template,redirect,request,url_for,flash
from flask_login import login_user,current_user,logout_user,login_required
from flask_wtf import form
from werkzeug.utils import append_slash_redirect
from forms import AddCarts, DeleteCart
import forms

from models import NewArrivals,MostSelling,AddCart
import secrets
import os
from __init__ import app,db


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
        form = AddCarts()
        return render_template('home/index.html',newarrival=newarrival,mostselling=mostselling,form=form)


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

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        Most = MostSelling.query.filter(MostSelling.title.like('%' + search + '%')).all()
        New = NewArrivals.query.filter(NewArrivals.title.like('%' + search + '%')).all()
        merged_list = Most + New
        
        return render_template('home/search.html',result=merged_list)

@views.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        number = request.form['number']
        address = request.form['address']
        current_user.number = number
        current_user.address = address
        db.session.commit()
        return redirect(url_for('views.Profile'))

@views.route('/cart', methods=['GET', 'POST'])
def cart():
    cart = AddCart.query.filter_by(user_id=current_user.id).all()
    items=[]
    total=0
    form = DeleteCart()

    if cart != []:
        for i in cart:
            if(i.type == 'New Arrivals'):
                items.append( NewArrivals.query.filter_by(id=i.item_id).first())
                total += NewArrivals.query.filter_by(id=i.item_id).first().price
            elif(i.type == 'Most Selling Collection'):
                items.append( MostSelling.query.filter_by(id=i.item_id).first())
                total += MostSelling.query.filter_by(id=i.item_id).first().discount
        if request.method == 'POST':
            if form.validate_on_submit():
                item_id = form.item_id.data
                item_type = form.type.data
                print(item_id,item_type)
                item = AddCart.query.filter_by(item_id=item_id,user_id=current_user.id,type=item_type).first()
                db.session.delete(item)
                db.session.commit()
                return redirect(url_for('views.cart'))
        return render_template('Cart/cart.html',items=items,total = total,form=form)

    else:
        return render_template('Cart/cart.html',items=items,total = total,form=form)


@views.route('/addcart', methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        form = AddCarts()
        if form.validate_on_submit():
            item_id = form.item_id.data,
            cart = AddCart(item_id=item_id,user_id=current_user.id,type=form.type.data)
            db.session.add(cart)
            db.session.commit()
            return redirect(url_for('views.home'))

    return 'apple'