from flask import Flask, jsonify, request

app = Flask(__name__)

messages = {}


@app.route('/', methods=['POST'])
def log():
    log_message = request.json
    messages[log_message['id']] = log_message['message']

    return jsonify({'status': 'success', "message": log_message['message']})


@app.route('/', methods=['GET'])
def get_messages():
    answ = list()
    for i in messages.keys():
        answ.append(messages[i])
    return jsonify({"message": answ})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
