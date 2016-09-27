
from flask import Flask
from flask import Blueprint, flash, g, session
from flask import request, redirect, url_for, render_template
from app import db

from app.mod_modem.models import Modem

bp_modem = Blueprint('modem', __name__, url_prefix='/modem')


@bp_modem.route('/<modemId>')
def modem(modemId):
    modem = Modem.query.filter_by(id=modemId).first()
    return render_template('modem.html', modem=modem)

@bp_modem.route('/add')
def add_modem():
    return render_template('add_modem.html')

@bp_modem.route('/post_modem', methods=['POST'])
def post_modem():
    # Create the modem object
    sim = request.form['sim']
    imei = request.form['imei']
    phone = request.form['phone']
    ip = request.form['ip']
    ssh = request.form['ssh_port']
    fw = request.form['firmware']

    modem = Modem(sim, imei, phone, ip, ssh, fw)
    db.session.add(modem)
    db.session.commit()

    return redirect(url_for('index'))



