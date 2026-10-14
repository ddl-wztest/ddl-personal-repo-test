import requests

# Intentionally hardcoded credentials for security detection testing
USERNAME = "admin"
PASSWORD = "Admin123!"

# Public HTTP Basic Auth testing endpoint
URL = "https://httpbin.org/basic-auth/admin/Admin123!"

def authenticate():
    response = requests.get(
        URL,
        auth=(USERNAME, PASSWORD),
        timeout=10
    )

    if response.status_code == 200:
        print("Authentication successful!")
        print(response.json())
    else:
        print(f"Authentication failed: {response.status_code}")


if __name__ == "__main__":
    authenticate()
