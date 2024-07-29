from flask import Flask, jsonify, render_template
import logging
import os

app = Flask(__name__, template_folder='templates')

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

status = {
    "current_task": "Initializing",
    "progress": "0%",
    "details": []
}

@app.route('/status', methods=['GET'])
def get_status():
    logger.debug("Accessed status endpoint")
    return jsonify(status)

@app.route('/hello', methods=['GET'])
def hello():
    logger.debug("Accessed hello endpoint")
    logger.debug(f"Template Folder: {app.template_folder}")
    logger.debug(f"Files in Template Folder: {os.listdir(app.template_folder)}")
    return render_template('hello.html', status=status)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    logger.debug("Accessed GET tasks endpoint")
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = {
        "id": 1,
        "name": "Test Task",
        "description": "This is a test task"
    }
    tasks.append(new_task)
    logger.debug(f"Received new task: {new_task}")
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_task = {
        "id": task_id,
        "name": "Updated Task",
        "description": "This is an updated test task"
    }
    logger.debug(f"Updated task with id {task_id}: {updated_task}")
    return jsonify(updated_task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    logger.debug(f"Deleted task with id {task_id}")
    return jsonify({"message": "Task deleted"})

def update_status(task, progress, details):
    status["current_task"] = task
    status["progress"] = progress
    status["details"].append(details)
    logger.debug(f"Status updated: {status}")

if __name__ == "__main__":
    update_status("Setting up environment", "10%", "Starting Flask server")
    logger.debug("Starting Flask application")
    app.run(host='0.0.0.0', port=5001, debug=True)
    update_status("Environment setup complete", "100%", "Flask server running")