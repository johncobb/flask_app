from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask import Blueprint
from app import db, app
from app.mod_auth.models import User
from app.mod_auth.models import Role


bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@bp_auth.route('/')
def index():
    return render_template('index.html')


@bp_auth.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()

    return render_template('profile.html',user=user) 

@bp_auth.route('/post_user', methods=['POST'])
def post_user():
    # Create the new user object
    user = User(request.form['username'], request.form['email'])
    # Add the user
    db.session.add(user)
    # Commit the transaction
    db.session.commit()
    
    return redirect(url_for('index'))


