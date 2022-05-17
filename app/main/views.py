from pickle import GET
from flask import abort, render_template
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Bikes, User, Reviews
from . import main
from .. import db,photos
from .forms import ReviewForm, UpdateProfile, BikeForm
from werkzeug.utils import secure_filename

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/updates.html',update_form =form)

@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(author = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))

@main.route('/reviews/<id>')
@login_required
def review(id):
    '''
    function to return the comments
    '''
    review =Reviews.get_review(id)
    print(review)
    title = 'reviews'
    return render_template('reviews.html', review = review,title = title)

@main.route('/new_review/<int:bikes_id>', methods = ['GET', 'POST'])
@login_required
def new_review(bikes_id):
    bikes = Bikes.query.filter_by(bikes_id = bikes_id).first()
    form = ReviewForm()

    if form.validate_on_submit():
        review = form.review.data

        new_review = Reviews(review=review,user_id=current_user.id, bikes_id=bikes_id)


        new_review.save_review()


        return redirect(url_for('main.index'))
    title='New Bike'
    return render_template('new_review.html',title=title,review_form = form,bikes_id=bikes_id)

# main.route('/new_bike<int:id>', methods=['GET','POST'])
# @login_required
# def new_bike():
    
#     title = 'Bike Hire'
    
#     form = BikeForm()
#     if form.validate_on_submit():
#         category = form.category.data
#         bike_pic= form.image
        
#         bike_obj = Bikes(category=category,bike_pic=bike_pic)
#         bike_obj.save()
#         return redirect(url_for('main.catalog'))
#     return render_template('new_bike.html', bike_form=form)


@main.route('/bike/', methods = ['GET','POST'])
@login_required
def new_bike():

    form = BikeForm()

    if form.validate_on_submit():
        category = form.category.data
        bike_pic= form.image
        
        bike_obj = Bikes(category=category,bike_pic=bike_pic)
        bike_obj.save()

        # Updated pitchinstance
        new_bike = Bikes(title=title,category= category,user_id=current_user.id,bike_pic=bike_pic)

        title='New Bike'

        new_bike.save_bike()

        return redirect(url_for('main.index')) #or main.bike ??

    return render_template('new_bike.html',bike_form= form)

@main.route('/categories/<category>')
def category(category):
    '''
    function to return the pitches by category
    '''
    category = Bikes.get_bikes(category) #get_bikes defined in the bikes route
    # print(category)
    title = f'{category}'
    return render_template('catalogue.html',title = title, category = category)
