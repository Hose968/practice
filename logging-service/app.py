from flask import Flask, jsonify, request
from hazelcast import HazelcastClient
import os

app = Flask(__name__)

hazelcast_node_address = os.environ.get('HAZELCAST_NODE_ADDRESS')

client = HazelcastClient(cluster_members=[hazelcast_node_address])
log_messages = client.get_map('log_messages').blocking()
log_messages.set("id", "text")


@app.route('/', methods=['POST'])
def log():
    message = request.json
    print(message)

    log_messages.put(message['id'], message['text'])

    return jsonify({'message': message['text'], 'status': 'logged'})


@app.route('/', methods=['GET'])
def get_messages():
    answ = list()

    for key, val in log_messages.entry_set():
        answ.append({key: val})

    return jsonify(answ)


if __name__ == '__main__':
    print(f"logging-service for {hazelcast_node_address} started!")
    app.run(host='0.0.0.0', port=5001)
