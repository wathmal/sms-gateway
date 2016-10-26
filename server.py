from messaging.sms import SmsSubmit
import serial
import os
from flask import Flask, jsonify, request
from functools import wraps
app = Flask(__name__)


def check_auth(username, password):
    """check username / pass"""
    return username == os.environ["SMS_GATEWAY_USER"] and password == os.environ["SMS_GATEWAY_PASS"]


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'message': 'not logged in'}), 404
        return f(*args, **kwargs)
    return decorated


def send_text(number, text, path='/dev/ttyUSB0'):
    sms = SmsSubmit(number, text)
    pdu = sms.to_pdu()[0]

    # print len(sms.to_pdu())

    # open the modem port (assumes Linux)
    ser = serial.Serial(path, timeout=1)
    # write the PDU length and wait 1 second till the
    # prompt appears (a more robust implementation
    # would wait till the prompt appeared)
    ser.write('AT+CMGS=%d\r' % pdu.length)
    print ser.readlines()
    # write the PDU and send a ctrl+z escape
    ser.write('%s\x1a' % pdu.pdu)
    ser.close()

# send_text('0719968892', 'anew mata baaa,, fuck gammu!')


@app.route("/")
def hello():
    return "python sms gateway :)"


@app.route('/send', methods=['POST'])
@requires_auth
def create_task():
    if not request.json or not 'number' in request.json:
        return jsonify({'message': 'no number provided'}), 400

    send_text(request.json['number'], request.json['text'])
    return jsonify({'message': 'message queued'}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
