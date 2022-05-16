from flask import abort, render_template
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import  User
from . import main
from .. import db
# from .forms import PitchForm,CommentForm, UpdateProfile
# from werkzeug.utils import secure_filename
@main.route('/')
def index():
    '''
    my index page
    return
    '''
    message= "Hello"
    title= 'Bike Hire!'
    return render_template('index.html', message=message,title=title)





