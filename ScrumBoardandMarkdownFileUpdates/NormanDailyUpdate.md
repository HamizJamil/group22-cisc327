# Norman Anderson

20073995

# MONDAY

1.  what is the branch he/she worked on (must be pushed to the repo)?

    -   norman_update_profile

2.  what is the progress so far (at least some test cases written, more than 2)?

    -   Fixing the backend to make it integrate with the frontend

3.  any difficulties.

    -   Work from previous sprints needs to be fixed before we can begin this
        sprint

4.  what is the plan for the days before the deadline?

    -   Need to have the backend (database) working with the frontend so that
        everybody else can work on the project

# TUESDAY

1.  what is the progress so far

    -   Sent the other team members my code so they can reformat it to conform
        to the course’s standards

2.  any difficulties.

    -   There are still a few bugs in the project such as messages flashing, but
        I figured they weren’t worth holding up everybody else any longer

3.  what is the plan for the days before the deadline?

    -   Begin creating functions for each of the tests

# WEDNESDAY

1.  what is the progress so far

    -   Had an online meeting with the team where we decided who’s going to
        write tests for which page

    -   Working on the front-end features such as messages flask.flash

2.  any difficulties.

    -   Having difficulty with messages flashing

3.  what is the plan for the days before the deadline?

    -   Satisfy the requirements of the second sprint for the backend

    -   Design tests for update_profile()

# THURSDAY

1.  what is the progress so far

    -   Team members have successfully merged my code into the format that we’re
        expected to deliver the project in.

    -   Had a Microsoft Teams meeting with a TA (Leo Song). He explained
        Selenium testing

2.  any difficulties.

-   There are a few frustrating HTML bugs that don’t cause problems on the new
    team project. Locally my code runs fine, but it doesn’t run the team’s tests
    properly, whereas the merged code in the repository passes the tests but has
    fronted and backend dysfunctionalities.

1.  what is the plan for the days before the deadline.

-   Start writing tests for profile_update() and make all the code work

# FRIDAY

1.  what is the progress so far

-   Tests are finally passing on my computer, and I’ve got the hang of Selenium
    testing

-   Had a zoom meeting with the prof, along with my team member Hamiz

1.  any difficulties.

-   Will, my team member created a Pull Request with his create_product tests,
    which run fine on his computer but don’t pass the tests on Github. We are
    trying to figure out what the problem is.

1.  what is the plan for the days before the deadline.

-   Figure out how to pass selenium tests on Github

# Saturday

1.  what is the progress so far

-   Hamiz, my team member, fixed the issue on Github. Turns out, the html files
    needed to be lowercased for the tests to call them properly.

-   Finishing up my update_profile test.

1.  any difficulties.

-   Tests were at first passing in the ide, but not through pytest. Turns out,
    the database is created and deleted every time pytest is run, so every user
    whose profile is meant to be updated in the update_profile test, needs to be
    created in the models.py backend test first. This solved the issue, and my
    tests are finally passing on Github.

1.  what is the plan for the days before the deadline.

-   A team member had problems with his update_product tests, so I have to fix
    the backend and html functions for that to work.

# Sunday

1.  what is the progress so far

-   Fixed update_product functionality in the morning.

1.  any difficulties.

-   Things are coming along nicely. This sprint should be submitted with no
    major issues.

1.  what is the plan for the days before the deadline.

-   Writing my documentation (doing it right now!) and doing a final review
    before submission.

# Test Cases

1.  **State Transition Test** – verifies that the user is able to navigate to
    the update profile page successfully.

| **Test ID** | **Test Scenarios**              | **Description**                                                      | **Test Step**                                                              | **Expected Result**                       | **Actual Result** | **Status**  |
|-------------|---------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------------|-------------------|-------------|
| 1           | User opening update profile tab | Selenium goes through the Navbar to open Account \>\> Update Profile | Open home page. Open Account tab on Navigation bar Click on Update profile | User should be in the update profile page | As expected       | PASS        |

1.  **Input Partitioning Testing** – Partition all possible input, correct and
    incorrect, and test each case i

| Test ID | Test Scenario                                                         | Output                                                      | Input to cause Output                      | Expected Result                                   | Actual Result | Status |
|---------|-----------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------|---------------------------------------------------|---------------|--------|
| 2       | Correct Set of Inputs by the user                                     | **Profile updated**                                         | All satisfying requirements                | Profile updated                                   | As expected   | PASS   |
| 3       | Incorrect username with space prefix                                  | **ERROR: No space as the prefix in new username**           | user_name = “ profiletest”                 | Profile not updated                               | As expected   | PASS   |
| 4       | Incorrect username with space suffix                                  | **ERROR: No space as suffix in new username**               | user_name = “profiletest ”                 | Profile not updated                               | As expected   | PASS   |
| 5       | Incorrect username with less than 2 characters                        | **ERROR: New username has to be longer than 2 characters**  | user_name = “p”                            | Profile not updated                               | As expected   | PASS   |
| 6       | Incorrect username longer than 20 characters                          | **ERROR: New username can’t be longer than 20 characters**  | user_name = “p”\*22                        | Profile not updated                               | As expected   | PASS   |
| 7       | Incorrect empty username                                              | **ERROR: New Username cannot be empty**                     | user_name = “”                             | Profile not updated                               | As expected   | PASS   |
| 8       | Incorrect username non alphanumeric                                   | **ERROR: Username has to be all alphanumeric**              | user_name = “prof!letest”                  | Profile not updated                               | As expected   | PASS   |
| 9       | Incorrect shipping address empty                                      | **ERROR: Shipping address cannot be empty**                 | Shipping_address=””                        | Profile not updated                               | As expected   | PASS   |
| 10      | Incorrect shipping address non alphanumeric                           | **ERROR: Shipping address has to be alphanumeric**          | Shipping_address=”Queen’s University !...” | Profile not updated                               | As expected   | PASS   |
| 11      | Correct postal code conversion lower-case to upper-case with no space | **Profile Updated**                                         | Postal_code=”K8l 3n6”                      | Postal code saved as “K8L3N6” and profile updated | As expected   | PASS   |
| 12      | Incorrect invalid Canadian postal code                                | **ERROR: Please enter a valid postal code**                 | Postal_code=”K2AA5Z9                       | Profile not updated                               | As expected   | PASS   |

1.  **Boundary Testing** – Since most of the error happens in the corner and
    boundary cases, Boundaries of postal code and username we

| Test ID | Test Scenario                                                     | Output                                                      | Input to cause Output | Expected Result     | Actual Result | Status |
|---------|-------------------------------------------------------------------|-------------------------------------------------------------|-----------------------|---------------------|---------------|--------|
| 13      | Correct username within the boundary: 20 characters               | **Profile updated**                                         | Username=”p” \* 20    | Profile updated     | As expected   | PASS   |
| 14      | Correct username within the boundary: 3 characters                | **Profile updated**                                         | Username=”ppp”        | Profile updated     | As expected   | PASS   |
| 15      | Incorrect username out of range: 21 characters                    | **ERROR: New username can’t be longer than 20 characters**  | Username=”p” \* 21    | Profile not updated | As expected   | PASS   |
| 16      | Incorrect username out of range: 2 characters                     | **ERROR: New username has to be longer than 2 characters**  | Username=”pp”         | Profile not updated | As expected   | PASS   |
| 17      | Correct Postal code: Correct length = 6, Follows X9X9X9           | **Profile updated**                                         | Postal_code=”K7L3N6”  | Profile updated     | As expected   | PASS   |
| 18      | Correct postal code: Correct length = 7, Follows X9X 9X9          | **Profile updated**                                         | Postal_code=”K7L 3N6” | Profile updated     | As expected   | PASS   |
| 19      | Incorrect postal code: correct length wrong order 9X9X9X          | **ERROR: Please enter a valid postal code**                 | Username=”3N6K7L”     | Profile not updated | As expected   | PASS   |
