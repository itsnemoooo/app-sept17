# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample endpoint returning JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'Hackathon Project',
        'description': 'This is a sample API response from Flask.',
    }
    return jsonify(data)

# Post data to the backend
@app.route('/api/data', methods=['POST'])
def post_data():
    json_data = request.get_json()
    return jsonify(message=f"Received data: {json_data['data']}")

if __name__ == '__main__':
    app.run(debug=True)
