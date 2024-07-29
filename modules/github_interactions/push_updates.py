import subprocess

def push_updates(branch_name):
    subprocess.run(["git", "push", "origin", branch_name], check=True)