def test_login_with_valid_credentials_returns_token(api, base_url):
    response = api.post(
        f"{base_url}/auth/login",
        json={"username": "demo", "password": "demo123"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["access_token"]

def test_login_with_invalid_password_returns_401(api, base_url):
    response = api.post(
        f"{base_url}/auth/login",
        json={"username": "demo", "password": "wrong-password"},
    )
    assert response.status_code == 401

def test_protected_endpoint_without_token_returns_401(api, base_url):
    response = api.get(f"{base_url}/protected/profile")
    assert response.status_code == 401

def test_protected_endpoint_with_invalid_token_returns_401(api, base_url):
    response = api.get(
        f"{base_url}/protected/profile",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert response.status_code == 401

def test_protected_endpoint_with_valid_token_returns_200(api, base_url):
    login = api.post(
        f"{base_url}/auth/login",
        json={"username": "demo", "password": "demo123"},
    )
    token = login.json()["access_token"]
    response = api.get(
        f"{base_url}/protected/profile",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["user"] == "demo"

def test_protected_endpoint_with_tampered_token_returns_401(api, base_url):
    response = api.get(
        f"{base_url}/protected/profile",
        headers={"Authorization": "Bearer invalid.token.modified"},
    )
    assert response.status_code == 401


def test_protected_endpoint_with_empty_bearer_token_returns_401(api, base_url):
    response = api.get(
        f"{base_url}/protected/profile",
        headers={"Authorization": "Bearer "},
    )
    assert response.status_code == 401


def test_protected_endpoint_with_wrong_auth_scheme_returns_401(api, base_url):
    response = api.get(
        f"{base_url}/protected/profile",
        headers={"Authorization": "Basic invalid-token"},
    )
    assert response.status_code == 401


def test_login_with_empty_credentials_returns_401(api, base_url):
    response = api.post(
        f"{base_url}/auth/login",
        json={"username": "", "password": ""},
    )
    assert response.status_code == 401
