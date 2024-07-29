from github import Github

def create_repository(token, repo_name):
    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(repo_name)
    return repo.clone_url