# LoanPro SDET Challenge

**Tester:** Juan de Dios Delgado

---

## Challenge References

* **Challenge:** https://gist.github.com/danielsilva-loanpro/db5fa96d70551c64f649e0faa79bf587
* **API Spec (OpenAPI):** https://gist.github.com/danielsilva-loanpro/f72a5821113a53043967b373df3e9aef
* **Swagger Viewer:** https://editor.swagger.io (open and paste contents of sdet_challenge_api.yml to view)

---

## Project Structure

```text
loanpro-challenge/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_list_users.py
│   ├── test_create_user.py
│   ├── test_get_user.py
│   ├── test_update_user.py
│   └── test_delete_user.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── BUGS.md
├── TRACEABILITY_MATRIX.md
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
└── .env (not committed)
```

---

## Setup

### Prerequisites

* Python 3.11+
* Docker Desktop

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start the API

```bash
# Make sure Docker Desktop is running first
docker run -d -p 3000:3000 ghcr.io/danielsilva-loanpro/sdet-interview-challenge:latest

# Verify it is running
curl http://localhost:3000/dev/users
# Should return: []
```

### Run Tests

```bash
pytest -v
```

### Run against specific environment

```bash
TEST_ENV=dev pytest -v
TEST_ENV=prod pytest -v
```

---

## CI/CD

Tests run automatically on every push via GitHub Actions.
Dev and prod environments run in parallel.

Reports are generated for each run and stored as artifacts.  
They can be downloaded from the Actions tab in GitHub.

---

## Deliverables

| File                          | Description                                         |
| ----------------------------- | --------------------------------------------------- |
| `tests/`                      | Complete E2E test suite — 37 tests                  |
| `.github/workflows/tests.yml` | GitHub Actions pipeline — dev and prod parallel     |
| `BUGS.md`                     | Bug report — 8 bugs found                           |
| `TRACEABILITY_MATRIX.md`      | Requirements traceability — 37 tests mapped to spec |
| CI/CD Artifacts | HTML test reports generated on each run (available in GitHub Actions) |
---

## Test Results Summary

| Total Tests | Passed | Failed | Bugs Found |
| ----------- | ------ | ------ | ---------- |
| 37          | 29     | 8      | 8          |

> See `BUGS.md` and GitHub Issues for full bug details.
