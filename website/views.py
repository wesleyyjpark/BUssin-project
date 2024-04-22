from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Review
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('./home.html', user=current_user)

@views.route('/reviews')
def reviews():
    return render_template('./reviews.html', user=current_user)

@views.route('/write-review', methods=['GET', 'POST'])
def write_review():
    if request.method == 'POST':
        location = request.form.get("location-names")
        vendor = request.form.get("vendor-names")
        category = request.form.get("category-names")
        item = request.form.get("item-names")
        rating = request.form.get("rate")
        comment = request.form.get('review')
        print(location)
        print(vendor)
        print(category)
        print(item)
        print(rating)
        print(comment)
        if category == None and item == None:
            flash('Please select all fields', category='error')
        else:
            new_review = Review(location=location, vendor=vendor, category=category, item=item, rating=int(rating), comments=comment, user_id=current_user.id)
            db.session.add(new_review)
            db.session.commit()
            flash('Review submitted!', category='success')
    
    return render_template('./write_review.html', user=current_user)