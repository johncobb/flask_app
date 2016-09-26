# CREATE TABLE printers (printer_id INT NOT NULL AUTO_INCREMENT, ip VARCHAR(20),
# ssh INT, phone VARCHAR(10), sim VARCHAR(20), imei VARCHAR(20), firmware
# VARCHAR(10), last_update DATE)

from app import db

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

# Define the Modem model
class Modem(Base):
    __tablename__ = 'modems'
    sim = db.Column(db.String(20), nullable=False)
    imei = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    ssh_port = db.Column(db.Integer, nullable=False)
    firmware = db.Column(db.String(10), nullable=False)

    def __init__(self, sim, imei, phone, ip, ssh_port, firmware):
        self.sim = sim
        self.imei = imei
        self.phone = phone
        self.ip = ip
        self.ssh_port = ssh_port
        self.firmware = firmware

    def __repr__(self):
        return '<Modem %r>' % (self.name)

