import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_request():
    data = request.get_json()
    response_data = {key: value for key, value in data.items()}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()