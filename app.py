from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_data():
    data = {
        'message' : 'Hello, this is Flask server',
        'status' : 'success'
    }
    return jsonify(data), 200

@app.route('/api', methods=['GET'])
def get_api():
    api = {
        'message' : 'Hi this is api',
        'status' : 'success'
    }
    return jsonify(api), 201

if __name__ == '__main__':
    app.run(debug=True)