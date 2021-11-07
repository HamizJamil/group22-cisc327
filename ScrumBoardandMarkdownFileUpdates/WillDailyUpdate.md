# MONDAY

1.  what is the branch he/she worked on (must be pushed to the repo)?

    -   will_A4_Sprint

2.  what is the progress so far (at least some test cases written, more than 2)?

    -   currently learning selenium since it is new content for me

    -   also researching best blackbox methods suited for this function

3.  any difficulties.

    -   Our team has had some difficulties from past sprints so we are currently
        fixing that up which has made it difficult to make progress on this
        sprint

4.  what is the plan for the days before the deadline?

    -   Finish research of testing format and methods

    -   Start testing my test functions on example systems

    -   When our system is complete, I will integrate and format the testing on
        it

# TUESDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   finished my logic tables for my two pages of testing – total of 30 tests

2.  any difficulties.

    -   Got caught up fixing a lot of integration code from other members –
        affected research time

3.  what is the plan for the days before the deadline?

    -   Begin creating functions for each of the tests

# WEDNESDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   Starting my smokescreen tests and finally figured out the proper way to
        address button clicks to submit products to db

2.  any difficulties.

    -   Took a while to make sure fields were identified correctly – fixed bugs
        in HTML file so they are now properly accessible

3.  what is the plan for the days before the deadline.

    -   Finish up test cases for create product and focus on small bugs in other
        areas of code

# THURSDAY

1.  what is the progress so far (at least some test cases written, more than 2)

    -   Finished tests and all passed with local Pytest-s qbay_test command but
        would not pass in CI pipeline

2.  any difficulties.

    -   Have to rework MVC for A4

3.  what is the plan for the days before the deadline.

    -   Reconfigure MVC and HTML templates according to profs layout and retest

# FRIDAY

1.  what is the progress so far (at least some test cases written, more than 2)

2.  any difficulties.

3.  what is the plan for the days before the deadline.

# Test Cases

1.  **State Transition Test** – verifies that our product page has proper functionality when transitioning to homepage after successful creation or back to home with no commit if backbutton selected. Functional testing format that will give our team confidence in the build and further testing.

| **Test ID** | **Test Scenarios** | **Description**                                                                                               | **Test Step**                                                                                                                                                                                                                                                                                               | **Expected Result**                           | **Actual Result** | **Status**  |
|-------------|--------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|-------------------|-------------|
| 1           | Creating Product   | Test the create product functionality of our Qbay web application to ensure users can create products to sell | Create Dummy User Owner Navigate from register page to create-product page Enter valid title that is all numeric, no prefix or suffix space, size \< 80 char Enter valid description. That is larger than title and \< 2000 char Enter a valid price between \$10-\$10000CAD Click on create product button | Product should be successfully created        | As expected       | PASS        |
| 2           | Creating Product   | Test the create product functionality of our Qbay web application to ensure users can create products to sell | Create Dummy User Owner Navigate from register page to create-product page Enter valid title that is all numeric, no prefix or suffix space, size \< 80 char Enter valid description. That is larger than title and \< 2000 char Enter a valid price between \$10-\$10000CAD Click on BACK button           | Product should be NOT BE successfully created | As expected       | PASS        |

1.  **Boundary Value Tests** – will test the system and its boundaries to ensure
    the limits result in the proper results. On top of that it will expose any
    underlying integration issues.

| Test ID | Test Scenario  | Input                                    | Expected Result                        | Actual Result | Status |
|---------|----------------|------------------------------------------|----------------------------------------|---------------|--------|
| 3       | Create Product | **Product Title is 1 character**         | Product should be successfully created | As expected   | PASS   |
| 4       | Create Product | **Product Title is 80 Characters**       | Product should be successfully created | As expected   | PASS   |
| 5       | Create Product | **Product Description 20 characters**    | Product should be successfully created | As expected   | PASS   |
| 6       | Create Product | **Product Description 2000 characters**  | Product should be successfully created | As expected   | PASS   |
| 7       | Create Product | **Product Price is 10**                  | Product should be successfully created | As expected   | PASS   |
| 8       | Create Product | **Product Price is 10000**               | Product should be successfully created | As expected   | PASS   |

| Test ID | Test Scenario  | Input                                    | Expected Result                            | Actual Result | Status |
|---------|----------------|------------------------------------------|--------------------------------------------|---------------|--------|
| 9       | Create Product | **Product Title is 0 character**         | Product should NOT be successfully created | As expected   | PASS   |
| 10      | Create Product | **Product Title is 81 Characters**       | Product should NOT be successfully created | As expected   | PASS   |
| 11      | Create Product | **Product Description 19 characters**    | Product should NOT be successfully created | As expected   | PASS   |
| 12      | Create Product | **Product Description 2001 characters**  | Product should NOT be successfully created | As expected   | PASS   |
| 13      | Create Product | **Product Price is 9**                   | Product should NOT be successfully created | As expected   | PASS   |
| 14      | Create Product | **Product Price is 10001**               | Product should NOT be successfully created | As expected   | PASS   |

1.  **Decision Table Testing** – will identify all the rules that will allow for
    a product to be created and updated. This will highlight the requirements
    from A2.

| Test ID | Test Scenario  | Input                                                                                                                        | Expected Result                            | Actual Result | Status |
|---------|----------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|---------------|--------|
| 15      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 9**   | Product should NOT be successfully created | As expected   | PASS   |
| 16      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 10**  | Product should NOT be successfully created | As expected   | PASS   |
| 17      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 9**   | Product should NOT be successfully created | As expected   | PASS   |
| 18      | Create Product | **Email is not valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 10**  | Product should NOT be successfully created | As expected   | PASS   |
| 19      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 9**   | Product should NOT be successfully created | As expected   | PASS   |
| 20      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 10**  | Product should NOT be successfully created | As expected   | PASS   |
| 21      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 9**   | Product should NOT be successfully created | As expected   | PASS   |
| 22      | Create Product | **Email is not valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 10**  | Product should NOT be successfully created | As expected   | PASS   |
| 23      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 9**       | Product should NOT be successfully created | As expected   | PASS   |
| 24      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 19 characters**  **Product Price is 10**      | Product should NOT be successfully created | As expected   | PASS   |
| 25      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 9**       | Product should NOT be successfully created | As expected   | PASS   |
| 26      | Create Product | **Email is valid**  **Product Title is 81 Characters**   **Product Description 20 characters**  **Product Price is 10**      | Product should NOT be successfully created | As expected   | PASS   |
| 27      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 9**       | Product should NOT be successfully created | As expected   | PASS   |
| 28      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 19 characters**  **Product Price is 10**      | Product should NOT be successfully created | As expected   | PASS   |
| 29      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 9**       | Product should NOT be successfully created | As expected   | PASS   |
| 30      | Create Product | **Email is valid**  **Product Title is 80 Characters**   **Product Description 20 characters**  **Product Price is 10**      | Product should be successfully created     | As expected   | PASS   |
