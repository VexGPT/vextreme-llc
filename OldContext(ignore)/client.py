import requests
import time

SERVER_URL = "http://localhost:5001"

def send_command(command):
    response = requests.post(f"{SERVER_URL}/execute", json={'command': command})
    return response.json()

def get_status():
    response = requests.get(f"{SERVER_URL}/get_status")
    return response.json()

def main():
    while True:
        # Example command
        command = "echo Hello, World!"
        print(f"Sending command: {command}")
        result = send_command(command)
        print(f"Command result: {result}")

        # Get status update
        status = get_status()
        print(f"Status update: {status}")

        # Simulate delay between operations
        time.sleep(60)

if __name__ == "__main__":
    main()