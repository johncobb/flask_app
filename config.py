import os

# Statement for enabling the development environment
DEBUG = True


# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql://unison_printer:1qaz9ijn!@unison-printer-nvirginia-mysql-instance1.cq0yojlqiv43.us-east-1.rds.amazonaws.com/Printers'

# Run and In-Memory copy of database
SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

DATABASE_CONNECTION_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = 'secret'

# Secret key for signing cookies
SECRET_KEY = 'secret'
