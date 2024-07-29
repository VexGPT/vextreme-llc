import subprocess

def clone_repository(repo_url, clone_path):
    subprocess.run(["git", "clone", repo_url, clone_path], check=True)