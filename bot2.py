from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

constparam = ''

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    constparam = incoming_msg

    print(constparam)
    msg.body(constparam)

    return str(resp)


if __name__ == '__main__':
    app.run()