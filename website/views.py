from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Review
from . import db
from .foodRatings import addNewRating, removeRating
import sqlite3

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('./home.html', user=current_user)

@views.route('/reviews')
def reviews():
    conn = sqlite3.connect('ratings.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ratings")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('./reviews.html', user=current_user, data=data)

@views.route('/write-review', methods=['GET', 'POST'])
def write_review():
    if request.method == 'POST':
        location = request.form.get("location-names")
        vendor = request.form.get("vendor-names")
        category = request.form.get("category-names")
        item = request.form.get("item-names")
        rating = request.form.get("rate")
        comment = request.form.get('review')
        if location == None or vendor == None or category == None or item == None or (vendor[len(vendor)-11::] != "Dining Hall" and item == None):
            flash('Please select all fields', category='error')
        elif rating == None:
            flash('Please select a rating', category='error')
        else:
            new_review = Review(location=location, vendor=vendor, category=category, item=item, rating=int(rating), comments=comment, user_id=current_user.id)
            db.session.add(new_review)
            addNewRating(location, vendor, category, item, int(rating))
            db.session.commit()
            flash('Review submitted!', category='success')
    
    return render_template('./write_review.html', user=current_user)

@views.route('/my-reviews', methods=['GET', 'POST'])
def my_reviews():
    remove = False
    if request.method == 'POST':
        if request.form.get("remove-button") == 'clicked':
            remove = True
        elif request.form.get("cancel") == 'clicked':
            remove= False
        elif request.form.get("remove") == 'clicked':
            data = request.form.getlist("check")
            data = request.form.getlist("check")
            for i in data:
                review = Review.query.filter_by(id=i).first()
                location = review.location
                vendor = review.vendor
                category = review.category
                item = review.item
                rating = review.rating
                removeRating(location, vendor, category, item, rating)
                Review.query.filter_by(id = i).delete()
                db.session.commit()
            remove = False
    return render_template("./my_reviews.html", user=current_user, remove=remove)