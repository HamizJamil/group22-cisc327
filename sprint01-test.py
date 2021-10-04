from sprint01 import db
from sprint01 import User
from sprint01 import Product

db.create_all()  # creating database and columns from sprint01

ADMIN = User(id=0, username="WilliamKennedy-ADMIN", email="18wsk@queensu.ca", balance=300, buyer=False, seller=True)  # testing user entities
ADMIN_TWO = User(id=1, username="HamizJamil", email="18hj16@queensu.ca", balance=0, buyer=True, seller=False) 

iPhone11 = Product(product_ID=0, seller="WilliamKennedy-ADMIN", price=600, number_of_product=1,
                   product_title="iPhone11",
                   product_description='Brand New Never Opened iPhone 11 with 250GB of storage', verified_buyer='NONE',
                   dollars_made=0, verified_buyer_reviews='NONE')

db.session.add(ADMIN)
db.session.add(ADMIN_TWO)
db.session.add(iPhone11)
# adding rows to identified columns ^^ RUN ONCE TO INITIALIZE FILE THEN COMMENT OUT FOR QUERY

db.session.commit()  # permanent storage of items in database

print(User.query.all())  # looping through all rows in User column
print(Product.query.all())

