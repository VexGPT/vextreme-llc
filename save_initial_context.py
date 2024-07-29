import os
import json

initial_context = {
    "context": "Initial context setup for VexGPT",
    "details": {
        "tasks": [],
        "goals": []
    }
}

os.makedirs('Contexts', exist_ok=True)

with open('Contexts/initial_context.json', 'w') as f:
    json.dump(initial_context, f)

print("Initial context saved to Contexts/initial_context.json")