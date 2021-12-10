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
| 11   | http://127.0.0.1:8081/products               | N/A              | NO              |
| 12   | http://127.0.0.1:8081/updateproduct          | email            | NO              |
| 13   | http://127.0.0.1:8081/updateproduct          | title            | NO              |
| 14   | http://127.0.0.1:8081/updateproduct          | new_title        | NO              |
| 15   | http://127.0.0.1:8081/updateproduct          | new_price        | NO              |
| 16   | http://127.0.0.1:8081/registration           | user_email       | NO              |
| 17   | http://127.0.0.1:8081/registration           | user_name        | NO              |
| 18   | http://127.0.0.1:8081/registration           | user_pass        | NO              |


