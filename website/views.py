from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('./home.html', user=current_user)

@views.route('/reviews')
def reviews():
    return render_template('./reviews.html', user=current_user)

@views.route('/write-review', methods=['GET', 'POST'])
def write_review():
    
    
    return render_template('./write_review.html', user=current_user)