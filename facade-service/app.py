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

    output = dict()
    logg_service = choice(logging_service_url)

    with requests.Session() as sess:
        response = sess.post(logg_service, json=message)

    output['logger'] = logg_service
    output['response'] = response.json()

    return jsonify(output)


@app.route('/', methods=['GET'])
def get_messages():
    answ = dict()
    output = dict()
    logg_service = choice(logging_service_url)

    with requests.Session() as sess:
        mes_response = sess.get(messages_service_url)

    with requests.Session() as sess:
        log_response = sess.get(logg_service)

    answ['messages-service'] = mes_response.json()
    answ['logging-service'] = log_response.json()

    output['logger'] = logg_service
    output['get-response'] = answ

    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
