from flask import Blueprint, request, jsonify

# Define the blueprint
chat_bp = Blueprint('chat_bp', __name__)

# Manually handle OPTIONS requests for /chat
@chat_bp.route('/chat', methods=['OPTIONS'])
def options_chat():
    response = jsonify()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Chatbot POST route
@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    return jsonify({"response": "Hello, this is your chatbot!"})






