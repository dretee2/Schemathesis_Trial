# authentication.py

import requests
import os

def get_access_token():
    """Authenticate and return the Bearer token for the API."""
    url = "https://your-auth-endpoint.com/login"  # Replace with your actual auth endpoint
    payload = {
        "email": "preciousanthony1997@gmail.com",
        "password": "Adinlewa150497"
    }

    """os.getenv("API_EMAIL")
    os.getenv("API_PASSWORD")"""

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    # Modify this line according to how the token is returned
    return response.json()["data"]["access_token"]
