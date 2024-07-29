from flask import Flask, request, jsonify
import subprocess
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Endpoint to execute commands
@app.route('/execute', methods=['POST'])
def execute():
    data = request.json
    command = data.get('command')
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    # Execute the command
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to save context
@app.route('/save_context', methods=['POST'])
def save_context():
    context = request.json
    with open('context.json', 'w') as f:
        json.dump(context, f)
    return jsonify({'message': 'Context saved successfully'})

# Endpoint to load context
@app.route('/load_context', methods=['GET'])
def load_context():
    if os.path.exists('context.json'):
        with open('context.json', 'r') as f:
            context = json.load(f)
        return jsonify(context)
    return jsonify({'message': 'No context found'})

# Endpoint to simulate chat functionality
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    # Simulate a chat response (this would be where you integrate with the actual chat API)
    response = {"response": f"Echo: {message}"}
    return jsonify(response)

# Endpoint to receive status updates
@app.route('/status_update', methods=['POST'])
def status_update():
    update = request.json
    # Process the status update (e.g., log it, act on it, etc.)
    return jsonify({'message': 'Status update received'})

# Endpoint to get status
@app.route('/get_status', methods=['GET'])
def get_status():
    # Example status check implementation
    status = {
        'tests_passed': True,
        'last_commit': 'abc123',
        'ci_cd_status': 'success'
    }
    return jsonify(status)

# Ensure you have your API key for any third-party service you might use
HEROKU_API_KEY = os.getenv('HEROKU_API_KEY')
if HEROKU_API_KEY is None:
    print("Warning: HEROKU_API_KEY environment variable not set.")

if __name__ == '__main__':
    app.run(port=5001)