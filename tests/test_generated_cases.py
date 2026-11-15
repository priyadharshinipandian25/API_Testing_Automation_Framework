
import pytest
import requests
import uuid

from app.test_case_generator import generate_test_cases

payload = {
    "name": "Generated Test User",
    "email": f"generated_{uuid.uuid4().hex[:8]}@example.com"
}

test_cases = generate_test_cases(
    "POST",
    "http://127.0.0.1:8000/users",
    payload
)


@pytest.mark.parametrize(
    "case",
    test_cases,
    ids=lambda case: case["test"]
)
def test_generated_api_cases(case):
    response = requests.request(
        method=case["method"],
        url=case["url"],
        json=case.get("payload"),
        timeout=10
    )

    assert response.status_code == case["expected_status"], (
        f"{case['test']} failed: "
        f"Expected {case['expected_status']}, "
        f"Got {response.status_code}"
    )
