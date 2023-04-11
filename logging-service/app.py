from flask import Flask, jsonify, request
from hazelcast import HazelcastClient
import os

app = Flask(__name__)

hazelcast_node_address = os.environ.get('HAZELCAST_NODE_ADDRESS')
client = HazelcastClient(cluster_members=[hazelcast_node_address])
messages = client.get_map('messages').blocking()


@app.route('/', methods=['POST'])
def log():
    message = request.json
    try:
        for i in message.keys():
            messages.put(i, message[i])
            print(message[i])
    except Exception as e:
        return jsonify({'status': 'fail', "message": e})

    return jsonify({'status': 'success', "message": ''})


@app.route('/', methods=['GET'])
def get_messages():
    answ = list()
    for id_, text in messages.entry_set():
        answ.append({id_: text})
    return jsonify(answ)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
