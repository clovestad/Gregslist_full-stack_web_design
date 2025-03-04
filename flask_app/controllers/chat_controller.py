from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

# Define the blueprint
chat_bp = Blueprint('chat_bp', __name__)

# Chatbot POST route
@chat_bp.route('/chat', methods=['POST'])
@cross_origin()  # Allow CORS
def chat():
    user_message = request.json.get('message')
    return jsonify({"response": "Hello, this is your chatbot!"})

# Handle OPTIONS request for CORS preflight
@chat_bp.route('/chat', methods=['OPTIONS'])
@cross_origin()
def options_chat():
    response = jsonify()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response







