from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from datetime import date
app = Flask(__name__)

@app.route("/")
def hello():
    return "Wow, You are here!!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    tod = date.today()
    msg = request.form.get('Body')
    msg += 'Date received: '+ tod

    # Create reply
    resp = MessagingResponse()
    resp.message("Echo: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)