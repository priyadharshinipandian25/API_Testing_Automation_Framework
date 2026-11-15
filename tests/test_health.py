def test_health_endpoint_returns_ok(api, base_url):
    response = api.get(f"{base_url}/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "QA Practice API"
