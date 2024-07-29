import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DATABASE_URI = os.getenv('DATABASE_URL')

def load_config():
    config = Config()
    print(f"Loaded configuration: {config.__dict__}")
    return config