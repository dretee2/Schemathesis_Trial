import schemathesis
from schemathesis import from_uri

schema = from_uri("https://test-v2.tramatch.com/api/recommendations/v2/openapi.json")

@schema.parametrize()
def test_recommendations_api(case, auth_token):
    case.base_url = "https://test-v2.tramatch.com/api"
    case.headers["Authorization"] = f"Bearer {auth_token}"
    response = case.call()
    case.validate_response(response)