import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file))


SQLALCHEMY_DATABASE_URI = 'mysql://unison_printer:1qaz9ijn!@unison-printer-nvirginia-mysql-instance1.cq0yojlqiv43.us-east-1.rds.amazonaws.com/Printers'
DATABASE_CONNECTION_OPTIONS = {}

THREADS_PER_PAGE = 2
CSRF_ENABLED = True

CSRF_SESSION_KEY = 'secret'


SECRET_KEY = 'secret'
