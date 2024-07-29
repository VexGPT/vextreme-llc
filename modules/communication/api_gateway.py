from flask import Flask, request, jsonify
from Modules.processing import process_command
from utils.config_loader import load_config

config = load_config()
app = Flask(__name__)

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command')
    # Process the command
    response = process_command(command)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=config['api_gateway_port'])
