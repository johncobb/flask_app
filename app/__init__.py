from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app = Flask(__name__)
# Configuration
app.config.from_object('config')

# Define database object
db = SQLAlchemy(app)


from app.mod_auth.controllers import mod_auth as auth_module
#from app.mod_modem.controllers import mod_modem as modem_module
#app.register_blueprint(auth_module)

#db.create_all()

