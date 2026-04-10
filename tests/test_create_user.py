import requests
import os
from dotenv import load_dotenv


load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
TOKEN = os.getenv("AUTH_TOKEN", "mysecrettoken")


class TestCreateUser:

    # HAPPY PATH
    def test_returns_201(self, base_url, sample_user):
        response = requests.post(f"{base_url}/users", json=sample_user)
        assert response.status_code == 201

    def test_response_body_matches_input(self, base_url, sample_user):
        response = requests.post(f"{base_url}/users", json=sample_user)
        data = response.json()
        assert data["name"] == sample_user["name"]
        assert data["email"] == sample_user["email"]
        assert data["age"] == sample_user["age"]

    def test_response_schema_is_correct(self, base_url, sample_user):
        response = requests.post(f"{base_url}/users", json=sample_user)
        data = response.json()
        assert "name" in data
        assert "email" in data
        assert "age" in data
        assert isinstance(data["name"], str)
        assert isinstance(data["email"], str)
        assert isinstance(data["age"], int)

    # NEGATIVE TESTS
    def test_missing_name_returns_400(self, base_url):
        payload = {"email": "test@example.com", "age": 25}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_missing_email_returns_400(self, base_url):
        payload = {"name": "Test", "age": 25}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_missing_age_returns_400(self, base_url):
        payload = {"name": "Test", "email": "test@example.com"}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_empty_body_returns_400(self, base_url):
        response = requests.post(f"{base_url}/users", json={})
        assert response.status_code == 400

    def test_duplicate_email_returns_409(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        response = requests.post(f"{base_url}/users", json=sample_user)
        assert response.status_code == 409

    def test_invalid_email_format_returns_400(self, base_url):
        payload = {"name": "Test", "email": "not-an-email", "age": 25}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_age_zero_returns_400(self, base_url):
        payload = {"name": "Test", "email": "test@example.com", "age": 0}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_age_above_max_returns_400(self, base_url):
        payload = {"name": "Test", "email": "test@example.com", "age": 151}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    # BOUNDARY TESTS
    def test_age_minimum_boundary(self, base_url):
        """age=1 is the minimum valid value per spec."""
        payload = {"name": "Boundary", "email": "min.age@example.com", "age": 1}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 201
        requests.delete(f"{base_url}/users/min.age@example.com",
            headers={"Authentication": TOKEN})

    def test_age_maximum_boundary(self, base_url):
        """age=150 is the maximum valid value per spec."""
        payload = {"name": "Boundary", "email": "max.age@example.com", "age": 150}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 201
        requests.delete(f"{base_url}/users/max.age@example.com",
            headers={"Authentication": TOKEN})

    # EDGE CASES
    def test_age_negative_returns_400(self, base_url):
        payload = {"name": "Test", "email": "test@example.com", "age": -1}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_age_as_string_returns_400(self, base_url):
        payload = {"name": "Test", "email": "test@example.com", "age": "thirty"}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_empty_name_returns_400(self, base_url):
        payload = {"name": "", "email": "test@example.com", "age": 25}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_email_with_spaces_returns_400(self, base_url):
        payload = {"name": "Test", "email": "test @example.com", "age": 25}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code == 400

    def test_very_long_name_does_not_crash(self, base_url):
        """API must not return 500 for very long name."""
        payload = {"name": "A" * 1000, "email": "long@example.com", "age": 25}
        response = requests.post(f"{base_url}/users", json=payload)
        assert response.status_code in [201, 400]  # not 500
        if response.status_code == 201:
            requests.delete(f"{base_url}/users/long@example.com",
                headers={"Authentication": TOKEN})
