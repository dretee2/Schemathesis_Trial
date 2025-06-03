import schemathesis

schema = schemathesis.from_uri("https://test-v2.tramatch.com/api/recommendations/v2/openapi.json")

@schema.parametrize()
def test_petstore_api(case):
    case.base_url = "https://test-v2.tramatch.com/api"
    response = case.call()
    case.validate_response(response)