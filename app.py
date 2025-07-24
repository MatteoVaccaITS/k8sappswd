# Import the required libraries from Flask and flask_cors
from flask import Flask, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
# Enable CORS to allow cross-origin requests
CORS(app)

# Define a route for the root ('/')
@app.route('/')
def hello():
    # Return a JSON response with a welcome message
    return jsonify(message="CIAO DA K8S!!!!!!!!e ehheheheee")

# Start the application only if the file is run directly
if __name__ == '__main__':
    # The app runs on all network interfaces, port 5000, in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)

