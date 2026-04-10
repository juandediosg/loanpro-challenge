import requests


class TestListUsers:
    def test_returns_200(self, base_url):
        response = requests.get(f"{base_url}/users")
        assert response.status_code == 200

    def test_returns_json_array(self, base_url):
        response = requests.get(f"{base_url}/users")
        assert isinstance(response.json(), list)

    def test_created_user_appears_in_list(self, base_url, sample_user):
        # Arrange + Assert POST
        create_response = requests.post(f"{base_url}/users", json=sample_user)
        assert create_response.status_code == 201 

        # Act + Assert GET
        response = requests.get(f"{base_url}/users")
        emails = [u["email"] for u in response.json()]
        assert sample_user["email"] in emails

    def test_dev_and_prod_are_isolated(self, sample_user):
        """User created in dev must NOT appear in prod."""
        import os
        from dotenv import load_dotenv
        load_dotenv()
        base = os.getenv("BASE_URL", "http://localhost:3000")
        dev = f"{base}/dev"
        prod = f"{base}/prod"
        requests.post(f"{dev}/users", json=sample_user)
        prod_users = requests.get(f"{prod}/users").json()
        prod_emails = [u["email"] for u in prod_users]
        assert sample_user["email"] not in prod_emails

