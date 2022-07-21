from flask import Blueprint, render_template,redirect,request,url_for,flash
from flask_login import login_user,current_user,logout_user,login_required
from forms import ProductForm

from models import MostSelling, NewArrivals
from __init__ import db,login_manager
from views import save_pic

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.Login'))
    if current_user.username != 'Admin':
        return redirect(url_for('views.home'))
    else:
        product = ProductForm()
        if(product.validate_on_submit()):
            if(product.productType.data == "New Arrivals"):
                p = save_pic(product.image.data)
                newArrival = NewArrivals(title=product.title.data,description=product.description.data,image=p,price=product.price.data,productType=product.productType.data)
                db.session.add(newArrival)
                db.session.commit()
                flash('New Arrival Added!')
                return redirect(url_for('admin.dashboard'))
            if(product.productType.data == "Most Selling Collection"):
                p = save_pic(product.image.data)
                mostSelling = MostSelling(title=product.title.data,description=product.description.data,image=p,price=product.price.data,productType=product.productType.data, discount=product.discountPrice.data)
                db.session.add(mostSelling)
                db.session.commit()
                flash('Most Selling Added!')
                return redirect(url_for('admin.dashboard'))
        return render_template('admin/admin.html',product=product)

