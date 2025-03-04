from flask import Flask, render_template
from flask_cors import CORS
from controllers.chat_controller import chat_bp

app = Flask(__name__)

# Enable CORS globally
CORS(app, resources={r"/*": {"origins": "*"}})

# Register the blueprint
app.register_blueprint(chat_bp, url_prefix='/')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


