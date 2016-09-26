from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://unison_printer:1qaz9ijn!@unison-printer-nvirginia-mysql-instance1.cq0yojlqiv43.us-east-1.rds.amazonaws.com/Printers'
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True

db = SQLAlchemy(app)

#class(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True)
#    email = db.Column(db.String(120), unique=True)
#
#    def __init__(self, username, email):
#        self.username = username
#        self.email = email
#
#    def __repr__(self):
#        return '<User %r>' % self.username



# *** New Flask-Security Code ***
# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
# Uncomment and run server to add first user
#@app.before_first_request
#def create_user():
#    db.create_all()
#    user_datastore.create_user(email='john@cphandheld.com', password='password')
#    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()

    return render_template('profile.html',user=user) 

@app.route('/post_user', methods=['POST'])
def post_user():
    # Create the new user object
    user = User(request.form['username'], request.form['email'])
    # Add the user
    db.session.add(user)
    # Commit the transaction
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')


