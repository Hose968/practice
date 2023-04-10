from flask import Flask, jsonify, request
import requests
from bson import ObjectId
from random import choice

app = Flask(__name__)

logging_service_url = ['http://logging-service-1:5001/',
                       'http://logging-service-2:5001/',
                       'http://logging-service-3:5001/']
messages_service_url = 'http://messages-service:5002/'


@app.route('/', methods=['POST'])
def log():
    log_message = request.json['message']
    message = {str(ObjectId()): log_message}

    with requests.Session() as sess:
        response = sess.post(choice(logging_service_url), json=message)

    return jsonify(response.json())


@app.route('/', methods=['GET'])
def get_messages():
    with requests.Session() as sess:
        mes_response = sess.get(messages_service_url)

    with requests.Session() as sess:
        log_response = sess.get(choice(logging_service_url))

    answ = dict()

    answ['messages-service'] = mes_response.json()
    answ['logging-service'] = log_response.json()

    return jsonify(answ)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
