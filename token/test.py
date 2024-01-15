import gitlab

# anonymous read-only access for public resources (GitLab.com)
gl = gitlab.Gitlab()

# anonymous read-only access for public resources (self-hosted GitLab instance)
gl = gitlab.Gitlab('https://gitlab.com')

# private token or personal token authentication (GitLab.com)
gl = gitlab.Gitlab(private_token='JVNSESs8EwWRx5yDxM5q')

# private token or personal token authentication (self-hosted GitLab instance)
gl = gitlab.Gitlab(url='https://gitlab.example.com', private_token='JVNSESs8EwWRx5yDxM5q')

# oauth token authentication
gl = gitlab.Gitlab('https://gitlab.example.com', oauth_token='my_long_token_here')

# job token authentication (to be used in CI)
# bear in mind the limitations of the API endpoints it supports:
# https://docs.gitlab.com/ee/ci/jobs/ci_job_token.html
import os
gl = gitlab.Gitlab('https://gitlab.example.com', job_token=os.environ['CI_JOB_TOKEN'])

# Define your own custom user agent for requests
gl = gitlab.Gitlab('https://gitlab.example.com', user_agent='my-package/1.0.0')

# make an API request to create the gl.user object. This is not required but may be useful
# to validate your token authentication. Note that this will not work with job tokens.
gl.auth()

# Enable "debug" mode. This can be useful when trying to determine what
# information is being sent back and forth to the GitLab server.
# Note: this will cause credentials and other potentially sensitive
# information to be printed to the terminal.
gl.enable_debug()