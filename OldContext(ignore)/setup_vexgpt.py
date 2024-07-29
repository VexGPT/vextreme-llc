import os
import subprocess
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_virtual_environment():
    logger.debug("Creating virtual environment...")
    subprocess.run(['python', '-m', 'venv', 'venv'], check=True)

def install_dependencies():
    logger.debug("Installing dependencies...")
    venv_path = Path('venv') / 'Scripts' / 'pip' if os.name == 'nt' else Path('venv') / 'bin' / 'pip'
    requirements_path = Path('requirements.txt')
    if not requirements_path.is_file():
        logger.error(f"{requirements_path} does not exist")
        return
    subprocess.run([venv_path, 'install', '-r', str(requirements_path)], check=True)

def setup_environment_variables():
    logger.debug("Setting up environment variables...")
    with open('.env', 'w') as f:
        f.write("API_KEY=your_api_key\n")
        f.write("DATABASE_URL=your_database_url\n")
        f.write("FLASK_APP=app/main.py\n")
        f.write("FLASK_ENV=development\n")
        f.write("PORT=5001\n")

def run_flask_app():
    logger.debug("Running Flask application...")
    venv_python = Path('venv') / 'Scripts' / 'python' if os.name == 'nt' else Path('venv') / 'bin' / 'python'
    subprocess.run([venv_python, 'app/main.py'], check=True)

if __name__ == '__main__':
    create_virtual_environment()
    install_dependencies()
    setup_environment_variables()
    run_flask_app()