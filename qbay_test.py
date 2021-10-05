from qbay import db
from qbay import User
from qbay import Product

db.create_all()  # creating database and columns from qbay

ADMIN = User(id=0, username="WilliamKennedy-ADMIN", email="18wsk@queensu.ca") 
# testing user entity

iPhone11 = Product(product_ID=0, owner_email="WilliamKennedy-ADMIN", price=600, 
                   number_of_product=1, product_title="iPhone11",
                   product_description='Brand New iPhone 11 with" \
                   "250GB of storage')

db.session.add(ADMIN)  # adding rows to identified columns
db.session.add(iPhone11)


db.session.commit()  # permanent storage of items in database

print(User.query.all())  # looping through all rows in User column
print(Product.query.all())

