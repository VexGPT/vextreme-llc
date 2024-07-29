from clone_repo import clone_repository
from commit_changes import commit_changes
from push_updates import push_updates
from fetch_changes import fetch_changes
from create_repo import create_repository

class GitHubManager:
    def __init__(self, token):
        self.token = token

    def clone_repo(self, repo_url, clone_path):
        clone_repository(repo_url, clone_path)

    def commit_and_push_changes(self, commit_message, branch_name):
        commit_changes(commit_message)
        push_updates(branch_name)

    def fetch_and_update(self):
        fetch_changes()

    def create_new_repo(self, repo_name):
        return create_repository(self.token, repo_name)
    
    def setup_repo(configs):
        repo_url = configs["github_repo_url"]
        branch = configs["branch"]
        token = configs["github_token"]

        # Configure git to use the token for authentication
        repo_url_with_token = repo_url.replace("https://", f"https://{configs['github_username']}:{token}@")
        
        # Clone the repository
        subprocess.run(["git", "clone", repo_url_with_token])

        # Navigate into the repo directory
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        os.chdir(repo_name)

        # Checkout the specified branch
        subprocess.run(["git", "checkout", branch])

        print(f"Repository {repo_name} setup complete on branch {branch}")