import os
import json

def clear_dynamic_context():
    dynamic_context = {
        "context": "Cleared dynamic context",
        "details": {
            "tasks": [],
            "goals": []
        }
    }

    with open('Contexts/dynamic_context.json', 'w') as f:
        json.dump(dynamic_context, f)

    print("Dynamic context cleared.")

if __name__ == "__main__":
    clear_dynamic_context()