
from flask import Flask
from flask import Blueprint, flash, g, session
from flask import request, redirect, url_for, render_template
from app import db

from app.mod_modem.models import Modem

mod_modem = Blueprint('modem', __name__, url_prefix='/modem')


@mod_modem.route('/modem/<modemId>')
@login_required
def modem(modemId):
    modem = Modem.query.filter_by(id=modemId).first()
    return render_template('modem.html, modem=modem)


