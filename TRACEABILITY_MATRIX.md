# Traceability Matrix — User Management API

**Tester:** Juan de Dios Delgado  
**Spec:** sdet_challenge_api.yml  
**Environments:** dev, prod  

---

| REQ ID | Endpoint | Requirement | Test | Status |
|--------|----------|-------------|------|--------|
| GET-01 | GET /users | Returns 200 | test_returns_200 | PASS |
| GET-02 | GET /users | Returns JSON array | test_returns_json_array | PASS |
| GET-03 | GET /users | Created user appears in list | test_created_user_appears_in_list | PASS |
| GET-04 | GET /users | dev and prod are isolated | test_dev_and_prod_are_isolated | PASS |
| POST-01 | POST /users | Returns 201 on success | test_returns_201 | PASS |
| POST-02 | POST /users | Response body matches input | test_response_body_matches_input | PASS |
| POST-03 | POST /users | Response schema correct | test_response_schema_is_correct | PASS |
| POST-04 | POST /users | 400 missing name | test_missing_name_returns_400 | PASS |
| POST-05 | POST /users | 400 missing email | test_missing_email_returns_400 | PASS |
| POST-06 | POST /users | 400 missing age | test_missing_age_returns_400 | PASS |
| POST-07 | POST /users | 400 empty body | test_empty_body_returns_400 | PASS |
| POST-08 | POST /users | 409 duplicate email | test_duplicate_email_returns_409 | FAIL — BUG #1 |
| POST-09 | POST /users | 400 invalid email format | test_invalid_email_format_returns_400 | FAIL — BUG #3 |
| POST-10 | POST /users | 400 age = 0 | test_age_zero_returns_400 | PASS |
| POST-11 | POST /users | 400 age = 151 | test_age_above_max_returns_400 | PASS |
| POST-12 | POST /users | BOUNDARY: age=1 valid | test_age_minimum_boundary | PASS |
| POST-13 | POST /users | BOUNDARY: age=150 valid | test_age_maximum_boundary | PASS |
| POST-14 | POST /users | EDGE: age=-1 returns 400 | test_age_negative_returns_400 | PASS |
| POST-15 | POST /users | EDGE: age as string returns 400 | test_age_as_string_returns_400 | PASS |
| POST-16 | POST /users | EDGE: empty name returns 400 | test_empty_name_returns_400 | PASS |
| POST-17 | POST /users | EDGE: email with spaces returns 400 | test_email_with_spaces_returns_400 | FAIL — BUG #4 |
| POST-18 | POST /users | EDGE: very long name handled | test_very_long_name_does_not_crash | PASS |
| GETU-01 | GET /users/{email} | 200 existing user | test_get_existing_user_returns_200 | PASS |
| GETU-02 | GET /users/{email} | Data matches | test_get_user_returns_correct_data | PASS |
| GETU-03 | GET /users/{email} | 404 not found | test_get_nonexistent_user_returns_404 | FAIL — BUG #5 |
| GETU-04 | GET /users/{email} | 404 has error field | test_404_response_has_error_field | PASS |
| PUT-01 | PUT /users/{email} | 200 on update | test_update_returns_200 | PASS |
| PUT-02 | PUT /users/{email} | Data persisted | test_update_data_is_persisted | FAIL — BUG #6 |
| PUT-03 | PUT /users/{email} | 404 not found | test_update_nonexistent_user_returns_404 | PASS |
| PUT-04 | PUT /users/{email} | 400 missing field | test_update_missing_field_returns_400 | PASS |
| PUT-05 | PUT /users/{email} | 400 invalid age | test_update_invalid_age_returns_400 | PASS |
| PUT-06 | PUT /users/{email} | 409 duplicate email | test_update_duplicate_email_returns_409 | PASS |
| DEL-01 | DELETE /users/{email} | 204 on delete | test_delete_returns_204 | PASS |
| DEL-02 | DELETE /users/{email} | User gone after delete | test_user_gone_after_delete | FAIL — BUG #7 |
| DEL-03 | DELETE /users/{email} | 401 no token | test_delete_without_token_returns_401 | FAIL — BUG #8 |
| DEL-04 | DELETE /users/{email} | 401 wrong token | test_delete_wrong_token_returns_401 | FAIL — BUG #8 |
| DEL-05 | DELETE /users/{email} | 404 not found | test_delete_nonexistent_user_returns_404 | PASS |

---

## Coverage Summary

| Category | Tests | Passed | Failed |
|----------|-------|--------|--------|
| Happy Path | 10 | 9 | 1 |
| Negative (4xx errors) | 15 | 11 | 4 |
| Boundary | 2 | 2 | 0 |
| Edge Cases | 6 | 5 | 1 |
| Security | 2 | 0 | 2 |
| **Total** | **37** | **29** | **8** |

> Failed tests indicate bugs. See BUGS.md and GitHub Issues for details.