#SQLmap test without cookies
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

#SQLmap test with cookies
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

1.  **🚢 Are all the user input fields in your application covered in all the
    test cases above? Any successful exploit?**
    
Yes, all user input fields within the application are covered within the test cases above. Within create product user_email, title, price and description were all cover. Within updateproduct email, title, new_title, new_price and new_description were all covered. Within updateprofile user_name, shipping_address and postal_code were all covered. Within registration user_email, user_pass and user_name were all covered. Within login user_email and user_pass were both covered. No successful exploits were found, this is shown in the console logs where all parameters are given an error asserting that they are non-injectable.

2.  **🚢 We did two rounds of scanning. Why the results are different? What is
    the purpose of adding in the session id?**

There is variance within the two difference at several points, however there is no variance in what parameters were covered as our application does not contain any fields that are only accessible to logged in users. The purpose of adding the session id in the second test is to test fields whilst logged in as a valid user.

3.  **🚢 Summarize the injection payload used based on the logs, and briefly
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