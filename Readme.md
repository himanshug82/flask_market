#Steps to Run in Dev Mode

$env:FLASK_APP = "market.py"

$env:FLASK_DEBUG=1

flask run

#database commands
from market import db
db.create_all()

from market import Item

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