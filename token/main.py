import os
from dotenv import load_dotenv
import requests

# Load environment variables from the .env file
load_dotenv()

# Get the GitLab deploy token and project ID from the environment
deploy_token = os.environ.get('DEPLOY_TOKEN')
project_id = os.environ.get('PROJECT_ID')

if not deploy_token:
    raise ValueError("DEPLOY_TOKEN environment variable not set.")
if not project_id:
    raise ValueError("PROJECT_ID environment variable not set.")

# Replace with your GitLab project URL and Deploy Token
gitlab_url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits"

# Define headers for authentication using "Private-Token"
headers = {
    "Private-Token": deploy_token,
}

# Define the GitLab project ID and any additional parameters (if needed)
params = {
    "all": "true",  # Include all commits, not just the latest
}

# Make the API request to retrieve commit data
response = requests.get(gitlab_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    commits = response.json()
    
    # Process the commit data as needed
    for commit in commits:
        author_name = commit['author_name']
        author_email = commit['author_email']
        commit_message = commit['message']
        
        # You can print or store the author data and commit message
        print(f"Author: {author_name} ({author_email})")
        print(f"Commit Message: {commit_message}")
else:
    print(f"Failed to retrieve commits. Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")