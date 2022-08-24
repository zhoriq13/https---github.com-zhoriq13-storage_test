from flask import Flask, request, jsonify
import json
import os
import tempfile

app = Flask(__name__)


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


@app.route('/')
def index():
    return "Some pretty cool text"


@app.route('/api/v1.0/storage/json/all', methods=['GET'])
def get_storage():
    data = read_data(os.path.join(tempfile.gettempdir(), 'storage.data'))
    return data


@app.route('/api/v1.0/storage/json/read', methods=['GET'])
def get_record():
    key = request.args.get('key')
    data = read_data(os.path.join(tempfile.gettempdir(), 'storage.data'))
    return data[key]


@app.route('/api/v1.0/storage/json/write', methods=['POST'])
def put_record():
    json_data = request.get_json()
    data = read_data(os.path.join(tempfile.gettempdir(), 'storage.data'))
    for i in json_data:
        if i in data:
            data[i].append(json_data[i])
        else:
            data[i] = [json_data[i]]
    write_data(os.path.join(tempfile.gettempdir(), 'storage.data'), data)
    return data, 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
