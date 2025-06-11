import schemathesis
from schemathesis import from_uri

schema = from_uri("https://test-v2.tramatch.com/api/alerts/v2/openapi.json")

@schema.parametrize()
def test_alerts_api(case, auth_token):
    case.headers["Authorization"] = f"Bearer {auth_token}"
    case.base_url = "https://test-v2.tramatch.com/api"
    response = case.call()
    case.validate_response(response)
