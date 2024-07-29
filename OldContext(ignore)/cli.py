import requests
import json

BASE_URL = "http://localhost:5001"

def chat(prompt):
    response = requests.post(f"{BASE_URL}/chat", json={"prompt": prompt})
    return response.json()

def save_context(context):
    response = requests.post(f"{BASE_URL}/save_context", json={"context": context})
    return response.json()

def load_context():
    response = requests.get(f"{BASE_URL}/load_context")
    return response.json()

if __name__ == "__main__":
    print("Welcome to Vex CLI")
    while True:
        command = input("Enter command (chat/save/load/exit): ")
        if command == "chat":
            prompt = input("Enter your message: ")
            response = chat(prompt)
            print("Vex:", response)
        elif command == "save":
            context_input = input("Enter context to save: ")
            # Ensure the context is a valid JSON
            try:
                context = json.loads(context_input)
                response = save_context(context)
                print(response)
            except json.JSONDecodeError:
                print("Invalid JSON format. Please enter a valid JSON string.")
        elif command == "load":
            response = load_context()
            print("Loaded context:", response)
        elif command == "exit":
            break
        else:
            print("Invalid command")