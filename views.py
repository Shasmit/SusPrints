from flask import Blueprint, render_template,redirect,request,url_for,flash

views = Blueprint('views', __name__)
@views.route('/')
def landingpage():
    return render_template('LandingPage/landingpage.html')