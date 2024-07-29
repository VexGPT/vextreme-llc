import subprocess

def fetch_changes():
    subprocess.run(["git", "fetch"], check=True)
    subprocess.run(["git", "pull"], check=True)