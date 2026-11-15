import os
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    """Set API_BASE_URL to test a different deployed test environment."""
    return os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")

@pytest.fixture
def api(base_url):
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()
