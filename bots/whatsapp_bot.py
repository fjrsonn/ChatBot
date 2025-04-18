from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from core.chat import get_response

whatsapp_app = Flask("whatsapp")

@whatsapp_app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body")
    resp = MessagingResponse()
    resp.message(get_response(msg))
    return str(resp)

if __name__ == "__main__":
    whatsapp_app.run(port=5001, debug=True)
