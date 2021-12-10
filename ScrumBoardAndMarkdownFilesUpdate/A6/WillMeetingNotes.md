# Wednesday 12/01/2021

1. what is the branch he/she worked on (must be pushed to the repo)?
  - Will\_A6\_Branch
2. what is the progress so far (at least some test cases written, more than 2)?
  - I have 3 main tasks:
    1. Driver for backend dev – finding way to display products that don&#39;t belong to current user and making sure that a proper transaction can happen with them (price \&lt; current balance)
    2. Backend tests – testing good/bad transaction and testing list display
    3. SQL injection testing
  - Right now I have completed meeting with Front-End and Controller Devs to make sure we are all on same page
    1. Just make function that returns list to be displayed -\&gt; frontend will format this list of objects in a table
    2. Update transaction to remove product and update price  can only pick from list (i)
  - Controller will handle the formatting from frontend
3. any difficulties.
  - None – really just supporting frontend to figure out how to extract product id from list displayed on page
4. what is the plan for the days before the deadline?
  - Execute Backend Dev with Hamiz as co-pilot
  - Create PR  have it approved
  - Then after weekend focus on SQL injection testing with SQLmap-dev when HTML updated

# Wednesday 12/09/2021

1. what is the branch he/she worked on (must be pushed to the repo)?
  - Will\_A6\_Branch
2. what is the progress so far (at least some test cases written, more than 2)?
  - I have completed backend dev now I wait for full completion of frontend to then begin security testing
3. any difficulties.
  - None – just ensuring that session id is accessed properly for SQL injection tests
4. what is the plan for the days before the deadline?
  - Complete SQL injection tests
  - Upload log to SQL injection folder
  - Upload MD scum meeting files and SCREENSHOTS
  - Submit
