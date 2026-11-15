import uuid

def unique_email():
    return f"qa_{uuid.uuid4().hex[:10]}@example.com"

def test_list_users_returns_list(api, base_url):
    response = api.get(f"{base_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_existing_user(api, base_url):
    response = api.get(f"{base_url}/users/1")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["name"]
    assert "@" in body["email"]

def test_get_missing_user_returns_404(api, base_url):
    response = api.get(f"{base_url}/users/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_user_returns_201(api, base_url):
    payload = {"name": "Test User", "email": unique_email()}
    response = api.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]
    assert isinstance(body["id"], int)

def test_duplicate_email_returns_409(api, base_url):
    email = unique_email()
    payload = {"name": "First User", "email": email}
    first = api.post(f"{base_url}/users", json=payload)
    assert first.status_code == 201
    second = api.post(f"{base_url}/users", json=payload)
    assert second.status_code == 409

def test_create_user_with_invalid_email_returns_422(api, base_url):
    response = api.post(
        f"{base_url}/users",
        json={"name": "Invalid Email", "email": "not-an-email"},
    )
    assert response.status_code == 422

def test_create_user_without_name_returns_422(api, base_url):
    response = api.post(
        f"{base_url}/users",
        json={"email": unique_email()},
    )
    assert response.status_code == 422

def test_put_replaces_user(api, base_url):
    created = api.post(
        f"{base_url}/users",
        json={"name": "Before Update", "email": unique_email()},
    )
    assert created.status_code == 201
    user_id = created.json()["id"]
    payload = {"name": "After PUT", "email": unique_email()}
    response = api.put(f"{base_url}/users/{user_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]
    assert response.json()["email"] == payload["email"]

def test_patch_updates_one_field(api, base_url):
    created = api.post(
        f"{base_url}/users",
        json={"name": "Before Patch", "email": unique_email()},
    )
    user_id = created.json()["id"]
    original_email = created.json()["email"]
    response = api.patch(
        f"{base_url}/users/{user_id}",
        json={"name": "After PATCH"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "After PATCH"
    assert response.json()["email"] == original_email

def test_delete_user_returns_204_and_then_404(api, base_url):
    created = api.post(
        f"{base_url}/users",
        json={"name": "To Delete", "email": unique_email()},
    )
    user_id = created.json()["id"]
    deleted = api.delete(f"{base_url}/users/{user_id}")
    assert deleted.status_code == 204
    follow_up = api.get(f"{base_url}/users/{user_id}")
    assert follow_up.status_code == 404
