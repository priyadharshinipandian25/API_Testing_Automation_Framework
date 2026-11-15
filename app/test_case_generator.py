
def generate_test_cases(method, url, payload=None):
    method = method.upper()

    expected_codes = {
        "GET": 200,
        "POST": 201,
        "PUT": 200,
        "PATCH": 200,
        "DELETE": 204
    }

    test_cases = [
        {
            "test": "Invalid endpoint",
            "method": method,
            "url": url.rsplit("/", 1)[0] + "/unknown-endpoint",
            "expected_status": 404
        },
        {
            "test": "Unsupported HTTP method",
            "method": "TRACE",
            "url": url,
            "expected_status": 405
        }
    ]

    if method in ["POST", "PUT", "PATCH"]:
        test_cases.append({
            "test": "Empty request body",
            "method": method,
            "url": url,
            "payload": {},
            "expected_status": 422
        })

    if payload:
        test_cases.append({
            "test": "Valid payload",
            "method": method,
            "url": url,
            "payload": payload,
            "expected_status": expected_codes[method]
        })

    return test_cases


if __name__ == "__main__":
    cases = generate_test_cases(
        "POST",
        "http://127.0.0.1:8000/users",
        {
            "name": "Test User",
            "email": "test@example.com"
        }
    )

    for case in cases:
        print(case)
