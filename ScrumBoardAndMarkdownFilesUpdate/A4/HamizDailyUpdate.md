# MONDAY

1.  what is the branch he/she worked on (must be pushed to the repo)?

    -   test_login_a4

2.  what is the progress so far (at least some test cases written, more than 2)?

    -   Researching best black box methods suited for this function

    -   And currently learning selenium since it is new content

3.  any difficulties.

    -   Work from previous sprints needs to be fixed before we can begin this
        sprint

4.  what is the plan for the days before the deadline?

    -   Finish research of testing format and methods

    -   Start testing my test functions on example systems

    -   When our system is complete, I will integrate and format the testing on
        it

# TUESDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   Completed one logic table – 5 tests written

2.  any difficulties.

    -   Figuring out proper formatting of selenium test cases

3.  what is the plan for the days before the deadline?

    -   Begin creating functions for each of the tests

# WEDNESDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   Completed both logic tables – 20 tests written

2.  any difficulties.

    -   Had to navigate differences between each of the black box methods within
        testing

3.  what is the plan for the days before the deadline.

    -   Finish up test cases for create product and focus on small bugs in other
        areas of code

# THURSDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   Integrating test cases into code

2.  any difficulties.

-   Navigating proper syntax to match test case code

1.  what is the plan for the days before the deadline.

-   Finish implementing test cases and make sure they run smoothly

# FRIDAY

1.  what is the progress so far (at least some test cases written, more than 2)

-   Finishing up code in my own branch, pushing to main branch soon

1.  any difficulties.

-   Smooth sailing

1.  what is the plan for the days before the deadline.

-   Submit our A4 sprint

# Test Cases

1.  **State Transition Test** – verifies that the user is routed to the proper
    state on successful login and unsuccessful login attempts.

| **Test ID** | **Test Scenarios** | **Description**                                                                                                                                                                                                                                  | **Test Step**                                                                                                                                                                                                                                                                                                                                                                                                                          | **Expected Result**                        | **Actual Result** | **Status**  |
|-------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|-------------------|-------------|
| 1           | User Logging In    | Test the login functionality of our Qbay web application to ensure users can login with their email address and password following email/password requirements, and if credentials are correct qBay routes them to home page                     | Create Dummy User Owner Navigate to login page of qBay app Attempt to login with both email and password being non-empty Email must follow RFC 5322 requirements Password must be \> 6 characters, with minimum one upper/lowercase and special characters Username must be non-empty, alphanumeric, and spaces not allowed in prefix or suffix Username must be \> 2 and \< 20 characters Click on LOGIN button                       | User should be logged in successfully      | As expected       | PASS        |
| 2           | User Logging In    | Test the login functionality of our Qbay web application to ensure users can login with their email address and password following email/password requirements, and if credentials are incorrect qBay properly re-routes them back to login page | Create Dummy User Owner Navigate to login page of qBay app Attempt to login with both email and password being non-empty Email must follow RFC 5322 requirements Password must be \> 6 characters, with minimum one upper/lowercase and special characters Username must be non-empty, alphanumeric, and spaces not allowed in prefix or suffix Username must be \> 2 and \< 20 characters Password is INCORRECT Click on LOGIN button | User should NOT be logged in successfully  | As expected       | PASS        |

1.  **Output Partitioning Testing** – Partition all possible output into
    equivalence classes with something in common, choose inputs to produce/cause
    said outputs from the code

| Test ID | Test Scenario   | Output                                                   | Input to cause Output                      | Expected Result                 | Actual Result | Status   |
|---------|-----------------|----------------------------------------------------------|--------------------------------------------|---------------------------------|---------------|----------|
| 3       | User Logging In | **Cannot have empty email**                              | No Email Provided                          | User not logged in successfully | As expected   | PASS     |
| 4       | User Logging In | **Cannot have empty password**                           | No Password Provided                       | User not logged in successfully | As expected   | PASS     |
| 5       | User Logging In | **Email does not follow addr-spec defined in RFC 5322**  | Email without @                            | User not logged in successfully | As expected   | PASS     |
| 6       | User Logging In | **Email does not follow addr-spec defined in RFC 5322**  | Email without .com/.ca/.net/.org           | User not logged in successfully | As expected   | PASS     |
| 7       | User Logging In | **Email does not follow addr-spec defined in RFC 5322**  | Email contains special characters          | User not logged in successfully | As expected   | PASS     |
| 8       | User Logging In | **Password must have at least 1 uppercase character**    | Password input has no uppercase characters | User not logged in successfully | As expected   | PASS     |

| Test ID | Test Scenario   | Output                                                 | Input to Cause output                              | Expected Result                 | Actual Result | Status |
|---------|-----------------|--------------------------------------------------------|----------------------------------------------------|---------------------------------|---------------|--------|
| 9       | User Logging In | **Password must have at least 1 lowercase character**  | Password input with no lowercase characters        | User not logged in successfully | As expected   | PASS   |
| 10      | User Logging In | **User Successfully Logged in**                        | Email address and Password meet requirements above | User logged in successfully     | As expected   | PASS   |

1.  **Input Partitioning Testing** – Covering partitions of simplest input
    values and varying them as little as possible, and catching errors in
    requirements and exposing problems in specification

| Test ID | Test Scenario   | Input                                                                                                                                                                        | Expected Result                           | Actual Result | Status |
|---------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------|--------|
| 11      | User Logging In | **Email Address Empty**  **Password contains 1 uppercase, 1 lowercase, 1 special character, and has minimum length 6**                                                       | User should not be logged in successfully | As expected   | PASS   |
| 12      | User Logging In | **Email Address does not contain @**  **Password contains 1 uppercase, 1 lowercase, 1 special character, and has minimum length 6**                                          | User should not be logged in successfully | As expected   | PASS   |
| 13      | User Logging In | **Email Address does not contain .com/.ca/.net/.org**  **Password contains 1 uppercase, 1 lowercase, 1 special character, and has minimum length 6**                         | User should not be logged in successfully | As expected   | PASS   |
| 14      | User Logging In | **Email Address contains special characters**  **Password contains 1 uppercase, 1 lowercase, 1 special character, and has minimum length 6**                                 | User should not be logged in successfully | As expected   | PASS   |
| 15      | User Logging In | **Email address follows requirements**  **Password is empty**                                                                                                                | User should not be logged in successfully | As expected   | PASS   |
| 16      | User Logging In | **Email address follows requirements**  **Password is less than 6 characters**                                                                                               | User should not be logged in successfully | As expected   | PASS   |
| 17      | User Logging In | **Email address follows requirements**  **Password is greater than 6 characters, has at least one lowercase letter and special character, but has no uppercase letters**     | User should not be logged in successfully | As expected   | PASS   |
| 18      | User Logging In | **Email address follows requirements**  **Password is greater than 6 characters, has at least one lowercase letter and special character, but has no lowercase letters**     | User should not be logged in successfully | As expected   | PASS   |
| 19      | User Logging In | **Email address follows requirements**  **Password is greater than 6 characters, has at least one uppercase and lowercase letter, but no special characters**                | User should not be logged in successfully | As expected   | PASS   |
| 20      | User Logging In | **Email address follows requirements**  **Password follows requirements, but does not match user registered to email**                                                       | User should not be logged in successfully | As expected   | PASS   |
| 21      | User Logging In | **Email address follows requirements, but does not match user registered to password**   **Password follows requirements**                                                   |                                           | As expected   | PASS   |
| 22      | User Logging In | **Email address follows requirements**  **Password follows requirements**  **This email address is not registered**                                                          |                                           | As expected   | PASS   |
| 24      | User Logging In | **Email address follows requirements**  **Password is greater than 6 characters, has at least one uppercase and lowercase letters, and has at least one special character**  | User should be logged in successfully     | As expected   | PASS   |
