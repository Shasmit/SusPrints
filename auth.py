
import email
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_user,current_user, logout_user, login_required
from models import user as User
from forms import RegistrationForm,LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db, bcrypt

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def Register():
    form_signup = RegistrationForm()
    # if current_user.is_authenticated:
    #     return redirect(url_for("views.home"))
    if request.method == "POST":
        if form_signup.validate_on_submit():
            if User.query.filter_by(email=form_signup.email.data).first():
                flash("Email already exists", "Email-Used")
                return redirect(url_for("auth.Register"))
            elif User.query.filter_by(username=form_signup.username.data).first():
                flash("Username already exists", "Username-Used")
                return redirect(url_for("auth.Register"))
            else:
                hashed_password = bcrypt.generate_password_hash(
                    form_signup.password.data
                ).decode("utf-8")
                user = User(
                    username=form_signup.username.data,
                    email=form_signup.email.data,
                    password=hashed_password,
                )
                print(user)
                db.session.add(user)
                db.session.commit()
                flash(
                    "Your account has been created! You are now able to log in",
                    "success",
                )
                return redirect(url_for("auth.Login"))
    return render_template(
        "Signup/register.html",
        title="Signup",
        form_signup=form_signup,
    )


@auth.route("/login", methods=["GET", "POST"])
def Login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        user = User.query.filter_by(email=form_login.email.data).first()
        if not user:
            flash("No user found with that email", "Email-Not-Found")
            return redirect(url_for("auth.Login"))
        elif not bcrypt.check_password_hash(user.password, form_login.password.data):
            flash("Password is incorrect", "Password-Incorrect")
            return redirect(url_for("auth.Login"))        

        elif user and bcrypt.check_password_hash(
            user.password, form_login.password.data
        ):
            login_user(user, remember=True)
            next_page = request.args.get("next")
            if (current_user.username == "Admin"):
                print("hasjkdhkjahsjkdhjkashdjkash")
                return redirect(url_for("admin.dashboard"))
            else:
                return (
                    redirect(next_page)
                    if next_page
                    else redirect(url_for("views.home"))
                )
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")

    
    return render_template(
        "LoginPage/login.html",
        title="Login",
        form_login=form_login,
    )

@auth.route("/Logout")
def Logout():
    logout_user()
    return redirect(url_for("views.landingpage"))