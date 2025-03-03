from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_app.models.ollamaapi import chat_with_ollama  # Correct path for API logic

# Create the Blueprint for the chatbot route
chat_bp = Blueprint('chat', __name__)

# Enable CORS for this controller
CORS(chat_bp)

# Handle POST and OPTIONS requests for the /chat route
@chat_bp.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "CORS preflight OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    # Handle the POST request with user input
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        bot_response = chat_with_ollama(user_message)  # Call the chat function from the model
        response = jsonify({"response": bot_response})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


