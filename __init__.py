from flask import Blueprint
from .metadata import TEMPLATE_FOLDER, STATIC_FOLDER
from .initialization.sidebar import initialize_sidebar
from .initialization.settings import register_settings
bp = Blueprint('estate_core', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER, static_url_path="/static/estate_core")

# import your routes here...

from .routes.dashboard import property_configurations, properties
from .routes.public import index, about_us, contact_us, property_listing, developers

def init_extension(app, db):
    with app.app_context():
        db.create_all()
        register_settings()
        initialize_sidebar()
    return bp 