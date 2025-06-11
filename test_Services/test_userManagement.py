import schemathesis
from schemathesis import from_uri

schema = from_uri("https://test-v2.tramatch.com/api/usermgmt/v2/docs/doc.json")

# to run   schemathesis run https://test-v2.tramatch.com/api/usermgmt/v2/docs/doc.json --experimental=openapi-3.1 --hypothesis-max-examples=50 --junit-xml=reports/contract-report.xml --report=reports/report.html
@schema.parametrize()
def test_user_management_api(case, auth_token):
    case.base_url = "https://test-v2.tramatch.com/api"
    case.headers["Authorization"] = f"Bearer {auth_token}"
    response = case.call()
    case.validate_response(response)