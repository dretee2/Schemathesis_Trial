import schemathesis

schema = schemathesis.openapi.from_url("https://test-v2.tramatch.com/api/recommendations/v2/openapi.json")

@schema.parametrize()
def test_api(case):
    case.call_and_validate()  # Finds bugs automatically