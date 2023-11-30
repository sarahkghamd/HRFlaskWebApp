from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required  # so you can not get to the home page unless you login
def home():
    return render_template("home.html", user=current_user)
