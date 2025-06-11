import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()  # Optional: load variables from a .env file



@pytest.fixture(scope="session")
def auth_token():
    """Fetch auth token once per test session."""
    email = "preciousanthony1997@gmail.com"
    password = "Adinlewa150497"

    """email = os.getenv("API_EMAIL")
    password = os.getenv("API_PASSWORD")"""

    if not email or not password:
        raise ValueError("Missing environment variables: API_EMAIL or API_PASSWORD")

    response = requests.post(LOGIN_URL, json={"email": email, "password": password})

    if response.status_code != 200:
        raise RuntimeError(f"Failed to log in: {response.status_code} - {response.text}")

    token = response.json().get("access_token")
    if not token:
        raise RuntimeError("Login response did not contain an access token")
    return token

