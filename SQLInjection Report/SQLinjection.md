| **Scan** | **Route/URL**                         | **Parameter**    | **Number of Injection Trials** | **Number of Successful Trials** |
|----------|---------------------------------------|------------------|--------------------------------|---------------------------------|
| 1        | <http://127.0.0.1:8081/login>         | user_email       | 15                             | 0                               |
|          |                                       | user_pass        | 15                             | 0                               |
| 2        | <http://127.0.0.1:8081/registration>  | user_email       | 15                             | 0                               |
|          |                                       | user_pass        | 15                             | 0                               |
|          |                                       | user_name        | 15                             | 0                               |
| 3        | <http://127.0.0.1:8081/updateprofile> | user_name        | 15                             | 0                               |
|          |                                       | shipping_address | 15                             | 0                               |
|          |                                       | postal_code      | 15                             | 0                               |
| 4        | <http://127.0.0.1:8081/updateproduct> | email            | 15                             | 0                               |
|          |                                       | title            | 15                             | 0                               |
|          |                                       | new_title        | 15                             | 0                               |
|          |                                       | new_price        | 15                             | 0                               |
|          |                                       | new_description  | 15                             | 0                               |
| 5        | <http://127.0.0.1:8081/createproduct> | user_email       | 15                             | 0                               |
|          |                                       | title            | 15                             | 0                               |
|          |                                       | price            | 15                             | 0                               |
|          |                                       | description      | 15                             | 0                               |

# SQLmap Test

# SQLmap Test with Cookies

| **Scan** | **Route/URL**                         | **Parameter**    | **Number of Injection Trials** | **Number of Successful Trials** |
|----------|---------------------------------------|------------------|--------------------------------|---------------------------------|
| 1        | <http://127.0.0.1:8081/login>         | user_email       | 15                             | 0                               |
|          |                                       | user_pass        | 15                             | 0                               |
| 2        | <http://127.0.0.1:8081/registration>  | user_email       | 15                             | 0                               |
|          |                                       | user_pass        | 15                             | 0                               |
|          |                                       | user_name        | 15                             | 0                               |
| 3        | <http://127.0.0.1:8081/updateprofile> | user_name        | 15                             | 0                               |
|          |                                       | shipping_address | 15                             | 0                               |
|          |                                       | postal_code      | 15                             | 0                               |
| 4        | <http://127.0.0.1:8081/updateproduct> | email            | 15                             | 0                               |
|          |                                       | title            | 15                             | 0                               |
|          |                                       | new_title        | 15                             | 0                               |
|          |                                       | new_price        | 15                             | 0                               |
|          |                                       | new_description  | 15                             | 0                               |
| 5        | <http://127.0.0.1:8081/createproduct> | user_email       | 15                             | 0                               |
|          |                                       | title            | 15                             | 0                               |
|          |                                       | price            | 15                             | 0                               |
|          |                                       | description      | 15                             | 0                               |

# QUESTIONS

1.  **🚢 Are all the user input fields in your application covered in all the
    test cases above? Any successful exploit?**

Yes, every field is covered in the test cases above. In the login page both user
email and user password are tested. In registration user email, user password
and username are all tested. In update profile only username and shipping
address and postal code are updated per the customer request. In create product
and update product the titles, descriptions, prices and respective new prices,
new titles and new descriptions are all tested. Below the team has attached
screenshots of the app and its respective input blocks to confirm the inputs
that should be tested

Thankfully the sqlmap open-source tool did not return any exploits or vulnerable
data/parameters in the csv file or in the terminal. This is proven in the figure
below the describing that all errors are not injectable. The team confirmed with
the prof that this is indeed an acceptable result concluding that none of the
parameters were vulnerable.

![Graphical user interface, text, application, chat or text message Description
automatically generated](media/a6db0e104a1adc48e1954e481016c074.png)![Graphical
user interface, website Description automatically
generated](media/ba4de0fca62099bad19f47a40efbc108.png)![Graphical user
interface, website Description automatically
generated](media/2e0175d79ff0987eaa6fdc71a0e65e75.png)![Graphical user
interface, text, application Description automatically
generated](media/df717918f12b246bb5995a2d3fbeb44c.png)![Graphical user interface
Description automatically generated](media/c1d346b41a39a717891a8293b0a86034.png)

**![](media/9f6705303a84ff11644f07da4c64b293.png)**

1.  **🚢 We did two rounds of scanning. Why the results are different? What is
    the purpose of adding in the session id?**

    In the end after both rounds of scanning returned empty csv files and ERROR
    describing that no parameters appear injectable. The terminal outputs still
    did differentiate in a few different places. The tests without any
    predefined session for testing but used a generated cookie of a new user.
    The injection cookie tests involved using the “session_id” – which was the
    one provided in the terminal after I retrieved the cookie from the request
    headers of the index page.

    The purpose of adding the “session_id” is so the attacker (in this case the
    students deploying the exploit tool) can act as a valid user using their
    cookies which are files of user data stored in the computer of the user who
    owns that session id. If the attacker can modify elements of that cookie to
    then exploit security measures – in our case scan restricted elements that
    are only available after logging in. An example of this stated in the
    assignment description is the authentication function.

2.  **🚢 Summarize the injection payload used based on the logs, and briefly
    discuss the purpose.**

The payload used to test the system is broken down into 6 main SQL injection
types. The first being Boolean based, error based, UNION query based, stacked
queries, time-based blind SQL injections, and inline queries.

The Boolean based blind method is used to test and see if a parameter is used to
return a T/F result from the database without recovering data from the database.
It does this by forcing the app to return a different result depending on the
query and the result. If the HTTP response changes between a true/false return
query, then the attacker can assume the injection is working. There are two
approaches tested in Boolean based blind method and that was WHERE/HAVING
clauses and parameter replacement - two separate types of queries used to yield
different results.

The second method is error-based SQL injection. This method takes advantage of
the database management system. If there are database management system errors
being returned for any database-related – then that means they can (POTENTIALLY)
carry queries depending on their configuration. Then payloads can be used to
target vulnerable functions. This method is fast but limited since it can only
retrieve 200Bytes of data at a time. SQLmap payload tests against multiple
different types of database management systems. This includes MySQL, Microsoft
SQL, Oracle, PostgreSQL, Sybase systems.

Union queries involve using the UNION clause to extract extra information. This
is done by extending the original query sent to the database – the original is
used to retrieve the response and the UNION is used to request access to other
information. The original query must be vulnerable for this to work. SQLmap
performs 1-10 generic UNION queries on each parameter, all different attempts to
extract extra data from app inputs.

Stacked queries are performed by injecting extra queries after the original
vulnerable done. There is also the potential to add non query statements such as
INSERT or even DELETE to tables. This method can even be used to perform OS
commands on local system. SQLmap tests these queries on certain supported
platforms – this includes PostgreSQL and Microsoft SQL Server.

Time-based blind SQL injection is the same system as Boolean based blind SQL
injection however the response time is what determines the differentiation
between true or false not the HTTP response. Slower times generally mean True
and fast response generally means False. It is better used in non-statement
queries since Boolean based is not applicable. SQLmap applies this blind SQL
injection method on the following supported platforms – MySQL, PostgreSQL,
Microsoft SQL Server and Oracle.

Inline queries are nested queries within the original query. These are not very
popular since web protection is advanced now and would require a very specific
vulnerable design of the app. SQLmap tests ‘Generic Inline queries’ on each of
the tested parameters.
