# MONDAY

1.  what is the branch he/she worked on (must be pushed to the repo)?

    -   Brock-A4

2.  what is the progress so far (at least some test cases written, more than 2)?

    -   Researching best black box methods suited for these function

    -   Attempting to become comfortable with selenium

    -   Began fixing issue with html for registration and product update page

3.  any difficulties.

    -   Work from previous sprints needs to be fixed before we can begin this
        sprint

4.  what is the plan for the days before the deadline?

    -   Start testing my test functions on frontend via selenium

    -   When our system is complete, I will integrate and format the testing on
        it

# TUESDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   wrote structure for update product page

2.  any difficulties.

    -   Figuring out proper formatting of selenium test cases

    -   Not able to test if these tests are correct as there is an issue with
        frontend of update product

3.  what is the plan for the days before the deadline?

    -   Begin creating functions for each of the tests

# WEDNESDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   completed all of my selenium tests for register user (14 tests)

2.  any difficulties.

    -   Had to debug some issues with backend of register user so all
        requirements would pass

3.  what is the plan for the days before the deadline.

    -   Finish up test cases for update product

# THURSDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   started debugging update product

2.  any difficulties.

-   

1.  what is the plan for the days before the deadline.

-   Finish implementing test cases and make sure they run smoothly

# FRIDAY

1.  what is the progress so far (at least some test cases written, more than 2)

-   Finishing up update product tests

1.  any difficulties.

-   no

1.  what is the plan for the days before the deadline.

-   Submit our A4 sprint

# Test Cases

1.  **Smoke test**– verifies that the user is routed to the proper state on
    successful registration attempts.

| **Test ID** | **Test Scenarios**   | **Description**                                                                                                                        | **Test Step**                                                                                       | **Expected Result**           | **Actual Result** | **Status**  |
|-------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------|-------------------|-------------|
| 1           | Registering new user | Test the register user functionality of our Qbay web application to ensure users can register with their email address and a password  | Navigate to register page of qbay app Attempt to register a new user to the database Submit account | New user should be registered | As expected       | PASS        |

1.  **Output Partitioning Testing** – Partition all possible output into
    equivalence classes with something in common, choose inputs to produce/cause
    said outputs from the code

| Test ID | Test Scenario    | Output                                                   | Input to cause Output                     | Expected Result     | Actual Result | Status   |
|---------|------------------|----------------------------------------------------------|-------------------------------------------|---------------------|---------------|----------|
| 2       | Registering User | **Cannot have empty email**                              | No Email Provided                         | User not registered | As expected   | PASS     |
| 3       | Registering User | **Cannot have empty password**                           | No Password Provided                      | User not registered | As expected   | PASS     |
| 4       | Registering User | **Email does not follow addr-spec defined in RFC 5322**  | Email with no @ domain                    | User not registered | As expected   | PASS     |
| 5       | Registering User | **Password less than 6 characters**                      | Password input has less than 6 characters | User not registered | As expected   | PASS     |

| Test ID | Test Scenario    | Output                                                | Input to Cause output                           | Expected Result     | Actual Result | Status |
|---------|------------------|-------------------------------------------------------|-------------------------------------------------|---------------------|---------------|--------|
| 6       | Registering User | **Password must have atleast one special character**  | Password input with no special characters       | User not registered | As expected   | PASS   |
| 7       | Registering User | **Password has no lower case**                        | Password with no lowercase characters           | User not registered | As expected   | PASS   |
| 8       | Registering User | **Username is empty**                                 | Username empty                                  | User not registered | As expected   | PASS   |
| 9       | Registering User | **Username is not alphanumeric only**                 | Username containing “!”                         | User not registered | As expected   | PASS   |
| 10      | Registering User | **Username has space at suffix**                      | Input username with space at suffix             | User not registered | As expected   | PASS   |
| 11      | Registering User | **Username has space at prefix**                      | Input username with space at prefix             | User not registered | As expected   | PASS   |
| 12      | Registering User | **Username with over 20 characters**                  | User should not be registered                   | As expected         | As expected   | PASS   |
| 13      | Registering User | **Username less than 3 characters**                   | Input username with less than 3 characters      | User not registered | As expected   | PASS   |
| 14      | Registering User | **Repeated email**                                    | Attempt to register with same email as test \#1 | User not registered | As expected   | PASS   |

**Boundary Value Tests** – will test the system and its boundaries to ensure the
limits result in the proper results. On top of that it will expose any
underlying integration issues.

| **Test ID** | **Test Scenarios**   | **Description**                           | **Test Step**                                                                                                                                  | **Expected Result**           | **Actual Result** | **Status**  |
|-------------|----------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-------------------|-------------|
| 15          | Registering new user | Test the upper bounds of username length  | Navigate to register page of qbay app Attempt to register a new user to the database using 19 characters as the username length Submit account | New user should be registered | As expected       | PASS        |
| 16          | Registering new user | Test the lower bounds of username length  | Navigate to register page of qbay app Attempt to register a new user to the database using 19 characters as the username length Submit account | New user should be registered | As expected       | PASS        |

1.  **Smoke Test** – verifies whether the important features are working and
    that there is no bugs or unintended actions on the build. Functional testing
    format that will give our team confidence in the build and further testing.

| **Test ID** | **Test Scenarios** | **Description**                                                                                               | **Test Step**                                                                                                                                                                                                                                                    | **Expected Result**                          | **Actual Result** | **Status**  |
|-------------|--------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------------|-------------|
| 1           | Creating Product   | Test the update product functionality of our Qbay web application to ensure users can create products to sell | Navigate to update-product page Enter valid title that is all numeric, no prefix or suffix space, size \< 80 char Enter valid description. That is larger than title and \< 2000 char Enter a valid price between \$10-\$10000CAD Click on update product button | Product should be successfully update        | As expected       | PASS        |
| 2           | Creating Product   | Test the create product functionality of our Qbay web application to ensure users can create products to sell | Navigate to update-product page Enter valid title that is all numeric, no prefix or suffix space, size \< 80 char Enter valid description. That is larger than title and \< 2000 char Enter a valid price between \$10-\$10000CAD Click on BACK button           | Product should be NOT BE successfully update | As expected       | PASS        |

1.  **Boundary Value Tests** – will test the system and its boundaries to ensure
    the limits result in the proper results. On top of that it will expose any
    underlying integration issues.

| Test ID | Test Scenario  | Input                                    | Expected Result                       | Actual Result | Status |
|---------|----------------|------------------------------------------|---------------------------------------|---------------|--------|
| 3       | Create Product | **Product Title is 1 character**         | Product should be successfully update | As expected   | PASS   |
| 4       | Create Product | **Product Title is 80 Characters**       | Product should be successfully update | As expected   | PASS   |
| 5       | Create Product | **Product Description 20 characters**    | Product should be successfully update | As expected   | PASS   |
| 6       | Create Product | **Product Description 2000 characters**  | Product should be successfully update | As expected   | PASS   |
| 7       | Create Product | **Product Price is 10**                  | Product should be successfully update | As expected   | PASS   |
| 8       | Create Product | **Product Price is 10000**               | Product should be successfully update | As expected   | PASS   |

| Test ID | Test Scenario  | Input                                    | Expected Result                            | Actual Result | Status |
|---------|----------------|------------------------------------------|--------------------------------------------|---------------|--------|
| 9       | Create Product | **Product Title is 0 character**         | Product should NOT be successfully updated | As expected   | PASS   |
| 10      | Create Product | **Product Title is 81 Characters**       | Product should NOT be successfully updated | As expected   | PASS   |
| 11      | Create Product | **Product Description 19 characters**    | Product should NOT be successfully updated | As expected   | PASS   |
| 12      | Create Product | **Product Description 2001 characters**  | Product should NOT be successfully updated | As expected   | PASS   |
| 13      | Create Product | **Product Price is 9**                   | Product should NOT be successfully updated | As expected   | PASS   |
| 14      | Create Product | **Product Price is 10001**               | Product should NOT be successfully updated | As expected   | PASS   |

1.  **Decision Table Testing** – will identify all the rules that will allow for
    a product to be created and updated. This will highlight the requirements
    from A2.

| Test ID | Test Scenario  | Input                                                                                                                        | Expected Result                            | Actual Result | Status |
|---------|----------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|---------------|--------|
| 15      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 9**   | Product should NOT be successfully updated | As expected   | TBD    |
| 16      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 10**  | Product should NOT be successfully updated | As expected   | TBD    |
| 17      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 9**   | Product should NOT be successfully updated | As expected   | TBD    |
| 18      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 10**  | Product should NOT be successfully updated | As expected   | TBD    |
| 19      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 9**   | Product should NOT be successfully updated | As expected   | TBD    |
| 20      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 10**  | Product should NOT be successfully updated | As expected   | TBD    |
| 21      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 9**   | Product should NOT be successfully updated | As expected   |        |
| 22      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 10**  | Product should NOT be successfully updated | As expected   |        |
| 23      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 9**       | Product should NOT be successfully updated | As expected   |        |
| 24      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 10**      | Product should NOT be successfully updated | As expected   |        |
| 25      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 9**       | Product should NOT be successfully updated | As expected   |        |
| 26      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 10**      | Product should NOT be successfully updated | As expected   |        |
| 27      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 9**       | Product should NOT be successfully updated | As expected   |        |
| 28      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 10**      | Product should NOT be successfully updated | As expected   |        |
| 29      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 9**       | Product should NOT be successfully updated | As expected   |        |
| 30      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 10**      | Product should be successfully created     | As expected   |        |

