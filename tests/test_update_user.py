import requests
import os
from dotenv import load_dotenv


load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
TOKEN = os.getenv("AUTH_TOKEN", "mysecrettoken")

class TestUpdateUser:

    def test_update_returns_200(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        updated = {"name": "Updated Name", "email": sample_user["email"], "age": 35}
        response = requests.put(
            f"{base_url}/users/{sample_user["email"]}", json=updated)
        assert response.status_code == 200

    def test_update_data_is_persisted(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        updated = {"name": "Updated Name", "email": sample_user["email"], "age": 35}
        requests.put(f"{base_url}/users/{sample_user["email"]}", json=updated)
        response = requests.get(f"{base_url}/users/{sample_user["email"]}")
        assert response.json()["name"] == "Updated Name"
        assert response.json()["age"] == 35

    def test_update_nonexistent_user_returns_404(self, base_url):
        payload = {"name": "Test", "email": "nobody@nowhere.com", "age": 25}
        response = requests.put(
            f"{base_url}/users/nobody@nowhere.com", json=payload)
        assert response.status_code == 404

    def test_update_missing_field_returns_400(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        payload = {"name": "Updated", "email": sample_user["email"]}  # no age
        response = requests.put(
            f"{base_url}/users/{sample_user["email"]}", json=payload)
        assert response.status_code == 400

    def test_update_invalid_age_returns_400(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        payload = {"name": "Test", "email": sample_user["email"], "age": 999}
        response = requests.put(
            f"{base_url}/users/{sample_user["email"]}", json=payload)
        assert response.status_code == 400

    def test_update_duplicate_email_returns_409(self, base_url, sample_user):
        """Changing email to one that already exists returns 409."""
        requests.post(f"{base_url}/users", json=sample_user)
        second = {"name": "Second", "email": "second.update@example.com", "age": 25}
        requests.post(f"{base_url}/users", json=second)
        payload = {"name": "Second", "email": sample_user["email"], "age": 25}
        response = requests.put(
            f"{base_url}/users/second.update@example.com", json=payload)
        assert response.status_code == 409
        requests.delete(f"{base_url}/users/second.update@example.com",
            headers={"Authentication": TOKEN})
