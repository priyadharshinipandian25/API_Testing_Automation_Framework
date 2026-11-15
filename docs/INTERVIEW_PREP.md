# Interview Preparation

## 60-second project explanation

"My project is an API Testing and Automation Framework built using Postman, Python, Requests and Pytest. I created a demo REST API as the system under test and tested its health, user CRUD operations, input validation and token-based access scenarios. I first explored requests and responses manually in Postman, then automated repeatable checks with Pytest assertions. I also generated an HTML report showing the actual execution results. The project helped me understand HTTP methods, status codes, JSON response validation, positive and negative testing, and test automation."

## Common questions

**1. What is an API?**  
An API is an interface that allows software components to communicate using defined requests and responses.

**2. What is API testing?**  
It verifies that an API behaves according to its requirements, including response data, status codes, validation and error handling.

**3. What is the difference between GET and POST?**  
GET retrieves a resource. POST submits data, commonly to create a resource or trigger an operation.

**4. What is the difference between PUT and PATCH?**  
PUT generally replaces a resource representation. PATCH applies a partial update.

**5. What is a status code?**  
It is an HTTP response code describing the result of a request, such as 200, 201, 400, 401, 404 or 500.

**6. What is a positive test?**  
A test using valid input and expecting the intended successful behavior.

**7. What is a negative test?**  
A test using invalid, missing or unexpected input and checking that the API handles it correctly.

**8. What is Pytest?**  
A Python testing framework used to organize and execute tests and report assertion failures.

**9. Why automate API tests?**  
Automation makes repeatable checks faster and helps detect regressions when code changes.

**10. What is a limitation of this project?**  
The demo service stores data in memory and uses simplified authentication. It is intended for learning and demonstration, not production use.

## Interview honesty checklist

- Run the project yourself before claiming it is complete.
- Be able to explain at least one test from each module.
- Do not claim load testing, penetration testing or production deployment.
- Be ready to explain why a test passed or failed.
