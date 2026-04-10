import requests


class TestDeleteUser:

    def test_delete_returns_204(self, base_url, sample_user, auth_headers):
        requests.post(f"{base_url}/users", json=sample_user)
        response = requests.delete(
            f"{base_url}/users/{sample_user["email"]}",
            headers=auth_headers)
        assert response.status_code == 204

    def test_user_gone_after_delete(self, base_url, sample_user, auth_headers):
        requests.post(f"{base_url}/users", json=sample_user)
        requests.delete(
            f"{base_url}/users/{sample_user["email"]}",
            headers=auth_headers)
        response = requests.get(f"{base_url}/users/{sample_user["email"]}")
        assert response.status_code == 404

    def test_delete_without_token_returns_401(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        response = requests.delete(
            f"{base_url}/users/{sample_user["email"]}")
        assert response.status_code == 401

    def test_delete_wrong_token_returns_401(self, base_url, sample_user):
        requests.post(f"{base_url}/users", json=sample_user)
        response = requests.delete(
            f"{base_url}/users/{sample_user["email"]}",
            headers={"Authentication": "wrongtoken"})
        assert response.status_code == 401

    def test_delete_nonexistent_user_returns_404(self, base_url, auth_headers):
        response = requests.delete(
            f"{base_url}/users/nobody@nowhere.com",
            headers=auth_headers)
        assert response.status_code == 404
        