#database commands
from market.models import db

db.drop_all()
db.session.commit()
db.create_all()
db.session.commit()

from market.models import User,Item
User.query.all()
Item.query.all()

u1= User(username='himanshu', password_hash='123456', email_address='abc@test.com')
db.session.add(u1)
db.session.commit()

User.query.all()

item1 = Item(name="Phone", price=500, barcode="1234566", description="Phone")
item2 = Item(name="Laptop", price=1500, barcode="123144566", description="Laptop")
item3 = Item(name="Charger", price=50, barcode="123364566", description="Charger")
item4 = Item(name="Beer", price=5, barcode="1234326566", description="Beer")

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)

db.session.commit()

Item.query.all()