from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_messages():
    return jsonify({'message': 'This is a static message'})


@app.route('/', methods=['POST'])
def post_messages():
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
