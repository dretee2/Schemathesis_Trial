# Onboarding New Services for Schemathesis Contract Testing

## Step 1: Ensure OpenAPI spec is exposed
Each service should expose its schema via a public/local URL.

## Step 2: Create a test suite
Use this template in `contract_tests/`:

```python
schema = schemathesis.from_uri("<OPENAPI_URL>")
@schema.parametrize()
def test_service(case):
    case.base_url = "<SERVICE_BASE_URL>"
    response = case.call()
    case.validate_response(response)
    