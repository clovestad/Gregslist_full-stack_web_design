from flask import Flask, render_template
from flask_cors import CORS
from controllers.chat_controller import chat_bp

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS on all routes and allow localhost + 127.0.0.1
CORS(app, resources={r"/chat": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000"]}})

# Register the blueprint
app.register_blueprint(chat_bp, url_prefix='/')  # Registers the chat blueprint at the root URL

@app.route('/')
def home():
    return render_template('home.html')  # Home route, adjust with your actual HTML

if __name__ == '__main__':
    app.run(debug=True)

