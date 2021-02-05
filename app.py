from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return "Wow!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    now = datetime.now()
    msg = request.form.get('Body')
    now_dt = now.strftime("%d/%m/%Y %H:%M:%S")
    msg+='\n*Received on:* '+str(now_dt)

    print(msg)
    # Create reply
    resp = MessagingResponse()
    resp.message("*Echo:* {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)