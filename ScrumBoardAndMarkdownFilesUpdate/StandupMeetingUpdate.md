# WILLIAM KENNEDY
# Wednesday 11/17/2021

1.  what is the branch he/she worked on (must be pushed to the repo)?

    -   Will_A5_Branch

2.  what is the progress so far (at least some test cases written, more than 2)?

    -   I have completed the SQL test steps for both the cookie injection and
        regular SQL injection using SQLmap-dev download.

    -   I am also testing some of the XSS exploiting tools to make sure I have a
        thorough understanding of both

    -   I am also working on updating our authentication function in
        controllers.py to identify saved user sessions

3.  any difficulties.

    -   I am currently struggling to ensure that the cookie poisoning is in fact
        done correctly. The assignment says that it should expect different
        results however both yield a non-vulnerable result for all parameters

    -   I am also struggling at managing both the testing and the PR - during
        the meeting today I am requesting that the original member assigned to
        fix up the controller.py aide me in finishing this PR since they were
        initially assigned driver of controllers.py fix.

4.  what is the plan for the days before the deadline?

    -   As scrum master I will accept everyone’s daily meeting forms and convert
        it to md format and upload to git

    -   Once that is completed, I will continue to try and fix the
        authentication and cookie poisoning tests to ensure I have corrected
        results – will do my best to reach office ours or contact TA/prof for
        assistance/clarification.

    -   Then I and my co-pilot, will push what can be completed on that PR and
        assign two reviewers and prepare for any constructive feedback


# NORMAN ANDERSON
# Wednesday 11/17/2021
1. what is the branch he/she worked on (has to be pushed to the repo).
  - norman_A5_authenticate
2. what is the progress so far (at least some test cases written/some results/code available)?
  - cloned PwnXSS
  - Was able to scan my application and generate logs for the registration and login pages.
  - Met the prof today at his office hour to ask for help.
3. any difficulties.
  - Selenium testing from last sprint made us comment out a bunch of session[&#39;user&#39;] to make the tests work. The problem with the selenium tests were that the session.permanet = True wasn&#39;t effective in saving data to the database, and we had to rely on the backend tests that were done initially each time the tests ran, to generate the database for each session. This time, we need to uncomment those session[&#39;user&#39;] lines and figure out how to store data once a user logs in.
4. what is the plan for the days before the deadline?
  - Fix session problems
  - Finish up XSS security scans and logs and correct any backend issues we have.

# Brock Tureski
# Wednesday 11/17/2021
1. what is the progress so far (at least some test cases written, more than 2)
  - met with Hamiz to discuss docker
2. any difficulties.
  - Figuring out proper formatting of docker
3. what is the plan for the days before the deadline.
  - Work with Hamiz on docker
  - Start testing docker
  - When our system is complete, I will integrate and format the testing on it

# Hamiz Jamil
# Wednesday 11/17/2021
1. what is the branch he/she worked on (must be pushed to the repo)?
  - N/A
2. what is the progress so far (at least some test cases written, more than 2)?
  - Discussed docker with Brock yesterday, split tasks into 2 parts
3. any difficulties.
  - Understanding Docker as it&#39;s very new content to the both of us and we have never done any sort of deployment before
4. what is the plan for the days before the deadline?
  - Finish research of Docker
  - Follow outline in a5\_docker.md
  - Deploy the entire web application through docker with a web interface for easier 
