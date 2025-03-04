from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

# Define the blueprint for the chat route
chat_bp = Blueprint('chat', __name__)

# POST route for the chatbot
@chat_bp.route('/chat', methods=['POST'])
@cross_origin()  # Allow cross-origin requests
def chat():
    user_message = request.json.get('message')
    response_message = f"Hello, you said: {user_message}"  # You can integrate AI logic here
    return jsonify({"response": response_message})

# Handle OPTIONS request for CORS preflight
@chat_bp.route('/chat', methods=['OPTIONS'])
@cross_origin()
def options_chat():
    response = jsonify()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response









