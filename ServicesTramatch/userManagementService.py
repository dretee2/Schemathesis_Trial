import requests
import schemathesis

# Step 1: Define your schema
schema = schemathesis.from_uri("https://petstore.swagger.io/v2/swagger.json")  # replace if needed


# to run   schemathesis run https://test-v2.tramatch.com/api/usermgmt/v2/docs/doc.json --experimental=openapi-3.1 --hypothesis-max-examples=50 --junit-xml=reports/contract-report.xml --report=reports/report.html
@schema.parametrize()
def test_authenticated(case):
    response = case.call()
    case.validate_response(response)
