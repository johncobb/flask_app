from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask import Blueprint
from app import db
from app.mod_auth.models import User
from app.mod_auth.roles import Role



mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


# *** New Flask-Security Code ***
# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@mod_auth.route('/')
def index():
    return render_template('index.html')


@mod_auth.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()

    return render_template('profile.html',user=user) 

@mod_auth.route('/post_user', methods=['POST'])
def post_user():
    # Create the new user object
    user = User(request.form['username'], request.form['email'])
    # Add the user
    db.session.add(user)
    # Commit the transaction
    db.session.commit()
    
    return redirect(url_for('index'))


