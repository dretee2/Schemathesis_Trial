import schemathesis

schema = schemathesis.from_uri("https://petstore.swagger.io/v2/swagger.json")

@schema.parametrize()
def test_petstore_api(case):
    case.base_url = "https://petstore.swagger.io/v2"
    response = case.call()
    case.validate_response(response)