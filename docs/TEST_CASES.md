# API Test Cases

**Project:** API Testing & Automation Framework  
**Environment:** Local QA Practice API (`http://127.0.0.1:8000`)  
**Test type:** Functional, positive, negative, CRUD and authentication testing

| ID | Scenario | Method / Endpoint | Test data | Expected result |
|---|---|---|---|---|
| TC-001 | Health check | GET /health | None | 200; status is `ok` |
| TC-002 | List users | GET /users | None | 200; JSON array |
| TC-003 | Get existing user | GET /users/1 | ID 1 | 200; ID equals 1 |
| TC-004 | Get unknown user | GET /users/999999 | Unknown ID | 404 |
| TC-005 | Create user | POST /users | Valid name and email | 201; generated ID |
| TC-006 | Duplicate email | POST /users | Existing email | 409 |
| TC-007 | Invalid email | POST /users | `not-an-email` | 422 validation error |
| TC-008 | Missing name | POST /users | Email only | 422 validation error |
| TC-009 | Replace user | PUT /users/{id} | Valid full user object | 200; fields replaced |
| TC-010 | Partial update | PATCH /users/{id} | Name only | 200; name changed, email retained |
| TC-011 | Delete user | DELETE /users/{id} | Existing ID | 204; no response body |
| TC-012 | Verify deleted user | GET /users/{id} | Deleted ID | 404 |
| TC-013 | Valid login | POST /auth/login | demo / demo123 | 200; bearer token |
| TC-014 | Invalid login | POST /auth/login | Wrong password | 401 |
| TC-015 | Protected endpoint without token | GET /protected/profile | No token | 401 |
| TC-016 | Protected endpoint invalid token | GET /protected/profile | Invalid token | 401 |
| TC-017 | Protected endpoint valid token | GET /protected/profile | Valid demo token | 200; profile returned |

## Execution evidence

After running the tests, record the actual result, date, environment and any defect ID. Do not mark a test as passed unless it was executed and the observed result matched the expected result.
