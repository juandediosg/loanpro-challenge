import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "mysecrettoken")
ENV = os.getenv("TEST_ENV", "dev")

@pytest.fixture
def base_url():
    """Base URL for current environment (dev or prod)."""
    return f"{BASE_URL}/{ENV}"

@pytest.fixture
def auth_headers():
    """Auth token required for DELETE endpoint."""
    return {"Authentication": AUTH_TOKEN}

@pytest.fixture
def sample_user():
    """Standard test user reused across tests."""
    return {
        "name": "Test User",
        "email": "testuser.juandelgado@example.com",
        "age": 45
    }

@pytest.fixture(autouse=True)
def cleanup(auth_headers, sample_user):
    """
    Runs after EVERY test automatically (autouse=True).
    Deletes the test user from dev and prod after each test.
    This prevents tests from affecting each other.
    """
    yield
    # Teardown -- runs even if test fails
    email = sample_user["email"]
    for env in ["dev", "prod"]:
        requests.delete(
            f"{BASE_URL}/{env}/users/{email}",
            headers=auth_headers
        )
