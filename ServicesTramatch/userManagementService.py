import requests
import schemathesis

# Step 1: Define your schema
schema = schemathesis.from_uri("https://petstore.swagger.io/v2/swagger.json")  # replace if needed

# Step 2: Fetch token dynamically from auth endpoint
def fetch_token():
    url = "https://api.example.com/auth/token"  # 🔁 Change to your actual token endpoint
    credentials = {
        "username": "revelationjay02@gmail.com",
        "password": "Password@1"
    }
    response = requests.post(url, json=credentials)
    response.raise_for_status()  # Fail early if auth fails
    return response.json()["access_token"]

AUTH_TOKEN = fetch_token()

# Step 3: Run Schemathesis with auth header injected
@schema.parametrize()
def test_authenticated(case):
    case.headers["Authorization"] = f"Bearer {AUTH_TOKEN}"
    response = case.call()
    case.validate_response(response)
