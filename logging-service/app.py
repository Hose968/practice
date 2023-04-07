from flask import Flask, jsonify, request

app = Flask(__name__)

messages = {}


@app.route('/', methods=['POST'])
def log():
    log_message = request.json
    for i in log_message.keys():
        messages[i] = log_message[i]
        print(log_message[i])
    return jsonify({'status': 'success'})


@app.route('/', methods=['GET'])
def get_messages():
    answ = list()
    for i in messages.keys():
        answ.append(messages[i])
    return jsonify({"message": ', '.join(answ)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
