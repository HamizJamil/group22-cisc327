| scan | Route/URL                                    | Parameter        | XSS Successful? |
|------|----------------------------------------------|------------------|-----------------|
| 1    | http://127.0.0.1:8081/                       | N/A              | NO              |
| 2    | http://127.0.0.1:8081/updateprofile          | user_email       | NO              |
| 3    | http://127.0.0.1:8081/updateprofile          | user_name        | NO              |
| 4    | http://127.0.0.1:8081/updateprofile          | shipping_address | NO              |
| 5    | http://127.0.0.1:8081/updateprofile          | postal_code      | NO              |
| 6    | http://127.0.0.1:8081/login                  | user_email       | NO              |
| 7    | http://127.0.0.1:8081/login                  | user_pass        | NO              |
| 8    | http://127.0.0.1:8081/logout                 | N/A              | NO              |
| 9    | http://127.0.0.1:8081/create_product         | user_email       | YES             |
| 10   | http://127.0.0.1:8081/userhome               | N/A              | NO              |
| 11   | http://127.0.0.1:8081/updateproduct          | email            | NO              |
| 12   | http://127.0.0.1:8081/updateproduct          | title            | NO              |
| 13   | http://127.0.0.1:8081/updateproduct          | new_title        | NO              |
| 14   | http://127.0.0.1:8081/updateproduct          | new_price        | NO              |
| 15   | http://127.0.0.1:8081/registration           | user_email       | NO              |
| 16   | http://127.0.0.1:8081/registration           | user_name        | NO              |
| 17   | http://127.0.0.1:8081/registration           | user_pass        | NO              |

Q1) We did two rounds of scanning. Why the results are different?
` `What is the purpose of adding in the session id?


We log in with a user in our database to be able to access all the other pages
of our website, since creating a product, updating profile etc. won't make
sense without a user in our session. The purpose of adding the session id is to
be able to test and scan the website with a user in session.


Q2) re all the possible XSS (script injection)
links/routes covered in the table above?
(think about any links that will render user inputs, such as URL paramer,
cookies, flask flash calls). If not, are those link/pages vulnerable to XSS?


Yes, all the possible routes are in the table above.

