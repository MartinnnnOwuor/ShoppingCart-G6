from app import app, db
from models import User, Product, CartItem, Review
import random

def seed_database():
    with app.app_context():
        # Create 10 users
        users = []
        for i in range(1, 11):
            user = User(username=f"user{i}", email=f"user{i}@example.com")
            user.set_password(f"password{i}")
            users.append(user)
        db.session.add_all(users)

        # Create 10 products
        products = []
        for i in range(1, 11):
            product = Product(
                name=f"Product {i}",
                description=f"Description for product {i}",
                price=round(random.uniform(10, 1000), 2)
            )
            products.append(product)
        db.session.add_all(products)

        # Commit to get IDs for users and products
        db.session.commit()

        # Create 10 cart items
        cart_items = []
        for i in range(10):
            cart_item = CartItem(
                user_id=random.choice(users).id,
                product_id=random.choice(products).id,
                quantity=random.randint(1, 5)
            )
            cart_items.append(cart_item)
        db.session.add_all(cart_items)

        # Create 10 reviews
        reviews = []
        for i in range(10):
            review = Review(
                user_id=random.choice(users).id,
                product_id=random.choice(products).id,
                rating=random.randint(1, 5),
                comment=f"This is review {i+1} for the product."
            )
            reviews.append(review)
        db.session.add_all(reviews)

        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()