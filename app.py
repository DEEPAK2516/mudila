from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the received data
stored_data = {}

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    # Store the data (you can also perform additional actions here)
    stored_data.update(data)
    return "OK", 200

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(stored_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
