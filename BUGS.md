# Bug Report — User Management API

**Date:** 2026-04-09
**Tester:** Juan de Dios Delgado
**API:** ghcr.io/danielsilva-loanpro/sdet-interview-challenge:latest
**Spec:** sdet_challenge_api.yml

---

## Summary

| Total Tests | Passed | Failed | Bugs Found |
|-------------|--------|--------|------------|
| 37 | 29 | 8 | 8 |

---

## BUG-001: POST /users returns 500 instead of 409 for duplicate email

**Endpoint:** POST /dev/users  
**Severity:** High  
**GitHub Issue:** #1

**Test:** `tests/test_create_user.py::TestCreateUser::test_duplicate_email_returns_409`

**Expected:** Returns 409 when email already exists.  
**Actual:** Returns 500 Internal Server Error.  
**Spec:** /users > post > responses > 409

---

## BUG-002: PUT /users/{email} returns 200 instead of 409 for duplicate email

**Endpoint:** PUT /dev/users/{email}  
**Severity:** High  
**GitHub Issue:** #2

**Test:** `tests/test_update_user.py::TestUpdateUser::test_update_duplicate_email_returns_409`

**Expected:** Returns 409 when updating email to one that already exists.  
**Actual:** Returns 200 and allows duplicate email.  
**Spec:** /users/{email} > put > responses > 409

---

## BUG-003: POST /users accepts invalid email format

**Endpoint:** POST /dev/users  
**Severity:** Medium  
**GitHub Issue:** #3

**Test:** `tests/test_create_user.py::TestCreateUser::test_invalid_email_format_returns_400`

**Expected:** Returns 400 for invalid email format.  
**Actual:** Returns 500.  
**Spec:** components > schemas > CreateUserRequest > email > format: email

---

## BUG-004: POST /users accepts email with spaces

**Endpoint:** POST /dev/users  
**Severity:** Medium  
**GitHub Issue:** #4

**Test:** `tests/test_create_user.py::TestCreateUser::test_email_with_spaces_returns_400`

**Expected:** Returns 400 for email with spaces.  
**Actual:** Returns 500.  
**Spec:** components > schemas > CreateUserRequest > email > format: email

---

## BUG-005: GET /users/{email} returns 500 instead of 404 for non-existent user

**Endpoint:** GET /dev/users/{email}  
**Severity:** High  
**GitHub Issue:** #5

**Test:** `tests/test_get_user.py::TestGetUser::test_get_nonexistent_user_returns_404`

**Expected:** Returns 404 when user does not exist.  
**Actual:** Returns 500 Internal Server Error.  
**Spec:** /users/{email} > get > responses > 404

---

## BUG-006: PUT /users/{email} does not persist changes

**Endpoint:** PUT /dev/users/{email}  
**Severity:** High  
**GitHub Issue:** #6

**Test:** `tests/test_update_user.py::TestUpdateUser::test_update_data_is_persisted`

**Expected:** Returns 200 and saves changes.  
**Actual:** Returns 200 but data is not updated in database.  
**Spec:** /users/{email} > put > responses > 200

---

## BUG-007: GET /users/{email} returns 500 after user is deleted

**Endpoint:** GET /dev/users/{email}  
**Severity:** High  
**GitHub Issue:** #7

**Test:** `tests/test_delete_user.py::TestDeleteUser::test_user_gone_after_delete`

**Expected:** Returns 404 after user is deleted.  
**Actual:** Returns 500 Internal Server Error.  
**Spec:** /users/{email} > get > responses > 404

---

## BUG-008: DELETE /users/{email} does not validate authentication token

**Endpoint:** DELETE /dev/users/{email}  
**Severity:** Critical  
**GitHub Issue:** #8

**Tests:**  
- `tests/test_delete_user.py::TestDeleteUser::test_delete_without_token_returns_401`  
- `tests/test_delete_user.py::TestDeleteUser::test_delete_wrong_token_returns_401`

**Expected:** Returns 401 without valid token.  
**Actual:** Returns 204 and deletes user without authentication.  
**Spec:** /users/{email} > delete > parameters > Authentication header required