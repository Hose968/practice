from flask import Flask, jsonify, request
import requests
from bson import ObjectId

app = Flask(__name__)

logging_service_url = 'http://logging-service:5001/'
messages_service_url = 'http://messages-service:5002/'


@app.route('/', methods=['POST'])
def log():
    log_message = request.json['message']
    message = {str(ObjectId()): log_message}
    requests.post(logging_service_url, json=message)
    return jsonify({'status': 'success'})


@app.route('/', methods=['GET'])
def get_messages():
    mes_response = requests.get(messages_service_url)
    log_response = requests.get(logging_service_url)
    answ = list()
    answ.append(mes_response.json()['message'])
    answ.append(', ')
    answ.append(log_response.json()['message'])
    response = ''.join(answ)
    return jsonify({"message": response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
