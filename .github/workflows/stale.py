from datetime import datetime, timedelta
from github import Github, GithubException
import os

# Create a PyGithub instance using the GITHUB_TOKEN environment variable
g = Github(os.environ['GITHUB_TOKEN'])

# Define the number of days after which a PR is considered stale
DAYS_BEFORE_STALE = 21

# Get the repository using the repository owner and name
repo = g.get_repo('krishi0408/cd-pipeline-sample')

# Iterate through all open pull requests
for pr in repo.get_pulls(state='open'):
    # Calculate the age of the PR in days
    age = (datetime.now() - pr.updated_at).days
    
    # If the PR is stale, close it
    if age > DAYS_BEFORE_STALE:
        try:
            pr.edit(state='closed')
            pr.create_issue_comment('This pull request was automatically closed because it has been stale for more than 3 weeks.')
        except GithubException as e:
            print(e)
