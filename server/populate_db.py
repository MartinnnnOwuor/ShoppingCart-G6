import json
from app import create_app, db
from app.models import Product

app = create_app()

with app.app_context():
    db.create_all()
    with open('products.json', 'r') as f:
        products = json.load(f)
        for item in products:
            product = Product(
                nameOfProduct=item['nameOfProduct'],
                price=item['price'],
                imageUrl=item['imageUrl'],
                quantity=item['quantity']
            )
            db.session.add(product)
        db.session.commit()
