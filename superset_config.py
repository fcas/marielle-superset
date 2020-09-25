import os

AUTH_ROLE_PUBLIC = 'Public'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"

# Superset specific config
ROW_LIMIT = 5000
TOKEN = os.urandom(24)

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = TOKEN

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'sqlite:////app/.superset/superset.db'
# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 3600
WTF_CSRF_SECRET_KEY = TOKEN
# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

SESSION_COOKIE_HTTPONLY = False

SESSION_COOKIE_SAMESITE = 'None'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE')
RECAPTCHA_OPTIONS = {'theme': 'white'}
