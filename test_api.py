import requests
import logging

BASE_URL = 'http://localhost:5001'

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_get_tasks():
    print("Running test_get_tasks...")
    response = requests.get(f'{BASE_URL}/tasks')
    logger.debug(f'GET /tasks: {response.status_code} - {response.json()}')
    assert response.status_code == 200
    print('GET /tasks:', response.json())

def test_add_task():
    print("Running test_add_task...")
    new_task = {
        "id": 1,
        "name": "Test Task",
        "description": "This is a test task"
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task)
    logger.debug(f'POST /tasks: {response.status_code} - {response.json()}')
    assert response.status_code == 201
    print('POST /tasks:', response.json())

def test_update_task():
    print("Running test_update_task...")
    updated_task = {
        "name": "Updated Task"
    }
    response = requests.put(f'{BASE_URL}/tasks/1', json=updated_task)
    logger.debug(f'PUT /tasks/1: {response.status_code} - {response.json()}')
    assert response.status_code == 200
    print('PUT /tasks/1:', response.json())

def test_delete_task():
    print("Running test_delete_task...")
    response = requests.delete(f'{BASE_URL}/tasks/1')
    logger.debug(f'DELETE /tasks/1: {response.status_code} - {response.json()}')
    assert response.status_code == 200
    print('DELETE /tasks/1:', response.json())

if __name__ == '__main__':
    test_get_tasks()
    test_add_task()
    test_update_task()
    test_delete_task()
    print('All tests passed!')