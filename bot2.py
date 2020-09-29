from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    with open("data.json", "w") as outfile: 
        json.dump(str(incoming_msg), outfile)

    msg.body(incoming_msg)

    return str(resp)


if __name__ == '__main__':
    app.run()
