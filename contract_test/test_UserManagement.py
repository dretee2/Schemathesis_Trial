import schemathesis

schema = schemathesis.from_uri("https://test-v2.tramatch.com/api/usermgmt/v2/docs/doc.json")

@schema.parametrize()
def test_user_management_api(case):
    case.base_url = "https://test-v2.tramatch.com/api"
    response = case.call()
    case.validate_response(response)