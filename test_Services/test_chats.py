import schemathesis

schema = schemathesis.from_uri("https://test-v2.tramatch.com/api/chats/v2/openapi.json")

@schema.parametrize()
def test_chats_api(case, auth_token):
    case.headers["Authorization"] = f"Bearer {auth_token}"
    case.base_url = "https://test-v2.tramatch.com/api"
    response = case.call()
    case.validate_response(response)
