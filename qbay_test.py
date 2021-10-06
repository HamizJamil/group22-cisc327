from qbay import db
from qbay import User
from qbay import Product
from qbay import create_product
from qbay import update_product

db.create_all()  # creating database and columns from qbay

desc = 'Brand New iPhone 11 with 250GB of storage'
# iPhone11 = create_product("iPhone11", desc,"WilliamKennedy-ADMIN", 600)

update_product("iPhone11", 1400, "New IPhone11", "First iPhone on QBay")

print(Product.query.all())


