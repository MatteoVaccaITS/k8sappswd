# Import the required libraries from Flask and flask_cors
from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket

# Create a Flask app
app = Flask(__name__)
# Enable CORS to allow cross-origin requests
CORS(app)

# Define a route for the root ('/')
@app.route('/')
def hello():
    # Return a JSON response with a welcome message
    return jsonify(message="CIAO DA K8S!!!!!!!!e ehheheheee")

@app.route('/health')
def health_check():
    # Return a JSON response indicating the service is healthy
    return jsonify(status="healthy")        

@app.route('/hostname')
def get_hostname():
    msg = os.getenv('MESSAGE', 'Hello from k8s!')
    hostname = socket.gethostname()
    # Return a JSON response with the hostname and message
    return jsonify(hostname=hostname, message=msg)

# Start the application only if the file is run directly
if __name__ == '__main__':
    # The app runs on all network interfaces, port 5000, in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)

