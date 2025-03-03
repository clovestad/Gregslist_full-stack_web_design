from flask import Flask, render_template
from flask_cors import CORS
from app.controllers.chat_controller import chat_bp  # Import the chatbot routes

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register the Blueprint with the correct URL prefix
app.register_blueprint(chat_bp, url_prefix='/')  

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)
