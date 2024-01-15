# GitLab Commit Retrieval

This Python script is designed to interact with the GitLab API to retrieve commit data from a specified project. It utilizes the GitLab Deploy Token for authentication and requires specific environment variables to be set.

## Prerequisites

Before using this script, ensure that you have the following:

- Python installed on your machine.
- [python-dotenv](https://pypi.org/project/python-dotenv/) library installed. You can install it using:

  ```bash
  pip install python-dotenv
  ```

## Setup

1. Clone this repository to your local machine.
2. Create a `.env` file in the project's root directory with the following content:

    ```env
    DEPLOY_TOKEN=your_gitlab_deploy_token
    PROJECT_ID=your_gitlab_project_id
    ```

    Replace `your_gitlab_deploy_token` and `your_gitlab_project_id` with your actual GitLab deploy token and project ID.

## Usage

Run the script using the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of your Python script.

## Script Explanation

1. **Loading Environment Variables:** The script loads the GitLab deploy token and project ID from the `.env` file.

2. **API Request:** It constructs the GitLab API URL using the provided project ID and makes a GET request to retrieve commit data.

3. **Authentication:** The script uses the deploy token as the "Private-Token" in the headers for authentication.

4. **Processing Commit Data:** If the request is successful (HTTP status code 200), it processes the retrieved commit data. It prints out the author's name, email, and commit message for each commit.

5. **Error Handling:** If the request fails, it prints the status code and response content for debugging.

## Disclaimer

Ensure that you handle deploy tokens and project IDs securely. Do not expose them in your code or public repositories.

**Note:** This README assumes that you have already set up a GitLab project and obtained a deploy token. If not, refer to the GitLab documentation for guidance on obtaining a deploy token: [GitLab Deploy Tokens](https://docs.gitlab.com/ee/user/project/deploy_tokens.html)
