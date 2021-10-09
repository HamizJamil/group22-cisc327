from qbay import db
from qbay import User
from qbay import Product
from qbay import create_product
from qbay import update_product

db.create_all()  # creating database and columns from qbay

desc = 'Brand New iPhone 11 with 250GB of storage'
iPhone11 = create_product("iPhone11", desc,"WilliamKennedy-ADMIN", 600)

update_product("iPhone11", 1400, "New IPhone11", "First iPhone on QBay")
test_user = User()
print(test_user.register_user("test user", "testuser@gmail.com","John123"))
print(test_user.login("testuser@gmail.com", "John123"))
test_user2 = User() 
test_user2.register_user("second user", "secondtest@gmail.com", "Jimmy121")
print(test_user2.login("sao1319-=-x@gmail.csamd", "Jimmy121"))
print(Product.query.all())


