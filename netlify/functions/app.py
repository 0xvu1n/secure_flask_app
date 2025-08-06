import sys
import os

# Add the project root to the sys.path so that your Flask app can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main_app import app

from flask_netlify import create_wsgi_handler

# Create the WSGI handler for Netlify
handler = create_wsgi_handler(app)