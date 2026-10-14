import os
import requests

GITHUB_TOKEN = "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"
REPO_OWNER = "ddl-wztest"
REPO_NAME = "ddl-personal-repo-test"

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def get_commits():
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN environment variable is not set")

    response = requests.get(
        url,
        headers=headers,
        params={"per_page": 100},
        timeout=30
    )
    response.raise_for_status()

    commits = response.json()

    for commit in commits:
        sha = commit["sha"]
        message = commit["commit"]["message"]
        author = commit["commit"]["author"]["name"]
        date = commit["commit"]["author"]["date"]

        print(f"SHA: {sha}")
        print(f"Author: {author}")
        print(f"Date: {date}")
        print(f"Message: {message}")
        print("-" * 50)

if __name__ == "__main__":
    get_commits()
