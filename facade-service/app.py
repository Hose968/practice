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
    log_response = None
    output = dict()
    logg_service = None

    with requests.Session() as sess:
        mes_response = sess.post(messages_service_url, json=message)

    while not log_response:
        logg_service = choice(logging_service_url)

        try:
            with requests.Session() as sess:
                log_response = sess.post(logg_service, json=message)
        except Exception as e:
            print(f"Unable to connect to {logg_service}, reason = {e.__class__.__name__} : {e}")
            continue

    output['logger'] = logg_service
    output['logger_response'] = log_response.json()
    output['message-service-response'] = mes_response.json()

    return jsonify(output)


@app.route('/', methods=['GET'])
def get_messages():
    answ = dict()
    output = dict()
    logg_service = None
    log_response = None

    with requests.Session() as sess:
        mes_response = sess.get(messages_service_url)

    while not log_response:
        logg_service = choice(logging_service_url)

        try:
            with requests.Session() as sess:
                log_response = sess.get(logg_service)
        except Exception as e:
            print(f"Unable to connect to {logg_service}, reason = {e.__class__.__name__} : {e}")
            continue

    answ['messages-service-response'] = mes_response.json()
    answ['logging-service-response'] = log_response.json()

    output['logger'] = logg_service
    output['get-response'] = answ

    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
