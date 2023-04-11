from flask import Flask, jsonify, request
import requests
from bson import ObjectId

app = Flask(__name__)

logging_service_url = 'http://logging-service:5001/'
messages_service_url = 'http://messages-service:5002/'


@app.route('/', methods=['POST'])
def log():
    answer = dict()

    log_message = request.json['message']
    message = {"id": str(ObjectId()), "message": log_message}

    log_response = requests.post(logging_service_url, json=message)
    mes_response = requests.post(messages_service_url, json=message)

    answer['message'] = mes_response.json()
    answer['logger'] = log_response.json()

    return jsonify({'status': 'success', 'message': answer})


@app.route('/', methods=['GET'])
def get_messages():
    mes_response = requests.get(messages_service_url)
    log_response = requests.get(logging_service_url)

    answer = dict()

    answer['message'] = mes_response.json()
    answer['logger'] = log_response.json()

    return jsonify({"message": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
