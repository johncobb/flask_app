from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
#from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app = Flask(__name__)
# Configuration
app.config.from_object('config')

# Define database object
db = SQLAlchemy(app)


from app.mod_auth.controllers import bp_auth as bp_auth_module
from app.mod_modem.controllers import bp_modem as bp_modem_module
app.register_blueprint(bp_auth_module)
app.register_blueprint(bp_modem_module)
db.create_all()

