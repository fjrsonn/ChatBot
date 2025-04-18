from flask import Blueprint, request, jsonify
from core.chat import get_response

chat_blueprint = Blueprint("chat", __name__)

@chat_blueprint.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "").strip()
        if not message:
            return jsonify({"error": "Mensagem vazia."}), 400

        response = get_response(message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
