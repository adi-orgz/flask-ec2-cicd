from flask import Flask

app = Flask(__name__, template_folder='templates')

# Import routes after app creation to avoid circular imports
from app import routes
