from flask import Flask
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "yomama"

# Enable CORS for chatbot functionality
CORS(app, resources={r"/chat": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000"]}})

# Import controllers (must be after app initialization to prevent circular imports)
from flask_app.controllers import controller_user, controller_listing, controller_message
from flask_app.controllers.chat_controller import chat_bp

# Register the chatbot blueprint
app.register_blueprint(chat_bp, url_prefix='/')
