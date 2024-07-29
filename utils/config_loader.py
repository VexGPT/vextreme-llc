import json
import os
from dotenv import load_dotenv

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def load_all_configs():
    load_dotenv()  # Load environment variables from .env file
    main_config = load_config('config/config.json')
    github_config = load_config('config/github_config.json')

    github_config["github_token"] = os.getenv("GITHUB_TOKEN")
    
    return {**main_config, **github_config}