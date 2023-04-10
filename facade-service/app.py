from flask import Flask, jsonify, request
import requests
from bson import ObjectId
import random

app = Flask(__name__)

logging_service_urls = ['http://logging-service-1:5001/',
                        'http://logging-service-2:5002/',
                        'http://logging-service-3:5003/']
messages_service_url = 'http://messages-service:5004/'


@app.route('/', methods=['POST'])
def log():
    log_message = request.json['message']
    message = {"id": str(ObjectId()), "text": log_message}

    logging_service_url = random.choice(logging_service_urls)

    print(logging_service_url)

    requests.post(logging_service_url, data=message)

    return jsonify({'status': 'success'})


@app.route('/', methods=['GET'])
def get_messages():

    logging_service_url = random.choice(logging_service_urls)
    # print(logging_service_url+"\n\n")

    mes_response = requests.get(messages_service_url)
    log_response = requests.get(logging_service_url)

    answ = dict()
    answ['message-service'] = mes_response.json()
    answ['logging-service'] = log_response.json()

    return jsonify(answ)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
