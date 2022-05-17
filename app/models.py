from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer,primary_key = True)
        username = db.Column(db.String(255),index = True)
        email = db.Column(db.String(255),unique = True,index = True)
        bio = db.Column(db.String(255))
        profile_pic_path = db.Column(db.String())
        secure_password = db.Column(db.String(255),nullable = False)
        @property
        def set_password(self):
            raise AttributeError('You cannot read the password attribute')
        @set_password.setter
        def password(self, password):
            self.secure_password = generate_password_hash(password)

class Bikes(db.Model):
    __tablename__='bikes'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bike_category = db.Column(db.String(255))
    bike_pic_path = db.Column(db.String())
    bike_reviews = db.Relationship("reviews",backref="username")