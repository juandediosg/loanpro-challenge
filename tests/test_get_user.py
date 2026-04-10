import requests


class TestGetUser:

    def test_get_existing_user_returns_200(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        response = requests.get(f"{base_url}/users/{sample_user["email"]}")
        assert response.status_code == 200

    def test_get_user_returns_correct_data(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        response = requests.get(f"{base_url}/users/{sample_user["email"]}")
        data = response.json()
        assert data["name"] == sample_user["name"]
        assert data["email"] == sample_user["email"]
        assert data["age"] == sample_user["age"]

    def test_get_nonexistent_user_returns_404(self, base_url):
        response = requests.get(f"{base_url}/users/nobody@nowhere.com")
        assert response.status_code == 404

    def test_404_response_has_error_field(self, base_url):
        response = requests.get(f"{base_url}/users/nobody@nowhere.com")
        assert "error" in response.json()
