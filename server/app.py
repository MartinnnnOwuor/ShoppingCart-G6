# from flask import Flask, request, jsonify
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from flask_migrate import Migrate
# from flask_cors import CORS
# from models import db, User, Product, CartItem, Review
# import os

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/ekart.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')  # Use environment variable

# jwt = JWTManager(app)
# db.init_app(app)
# migrate = Migrate(app, db)
# CORS(app)

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.json
#     user = User(username=data['username'], email=data['email'])
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({"message": "User registered successfully"}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     user = User.query.filter_by(username=data['username']).first()
#     if user and user.check_password(data['password']):
#         access_token = create_access_token(identity=user.id)
#         return jsonify(access_token=access_token), 200
#     return jsonify({"message": "Invalid credentials"}), 401

# @app.route('/products', methods=['GET'])
# def get_products():
#     products = Product.query.all()
#     return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products])

# @app.route('/products/<int:product_id>', methods=['GET'])
# def get_product(product_id):
#     product = Product.query.get_or_404(product_id)
#     return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price})

# @app.route('/products', methods=['POST'])
# @jwt_required()
# def add_product():
#     data = request.json
#     new_product = Product(name=data['name'], description=data['description'], price=data['price'])
#     db.session.add(new_product)
#     db.session.commit()
#     return jsonify({"message": "Product added successfully", "id": new_product.id}), 201

# @app.route('/products/<int:product_id>', methods=['PUT'])
# @jwt_required()
# def update_product(product_id):
#     product = Product.query.get_or_404(product_id)
#     data = request.json
#     product.name = data.get('name', product.name)
#     product.description = data.get('description', product.description)
#     product.price = data.get('price', product.price)
#     db.session.commit()
#     return jsonify({"message": "Product updated successfully"})

# @app.route('/products/<int:product_id>', methods=['DELETE'])
# @jwt_required()
# def delete_product(product_id):
#     product = Product.query.get_or_404(product_id)
#     db.session.delete(product)
#     db.session.commit()
#     return jsonify({"message": "Product deleted successfully"})

# @app.route('/cart', methods=['GET'])
# @jwt_required()
# def get_cart():
#     user_id = get_jwt_identity()
#     cart_items = CartItem.query.filter_by(user_id=user_id).all()
#     return jsonify([{"id": item.id, "product_id": item.product_id, "quantity": item.quantity} for item in cart_items])

# @app.route('/cart', methods=['POST'])
# @jwt_required()
# def add_to_cart():
#     user_id = get_jwt_identity()
#     data = request.json
#     cart_item = CartItem(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
#     db.session.add(cart_item)
#     db.session.commit()
#     return jsonify({"message": "Item added to cart successfully", "id": cart_item.id}), 201

# @app.route('/cart/<int:item_id>', methods=['DELETE'])
# @jwt_required()
# def remove_from_cart(item_id):
#     user_id = get_jwt_identity()
#     cart_item = CartItem.query.filter_by(id=item_id, user_id=user_id).first_or_404()
#     db.session.delete(cart_item)
#     db.session.commit()
#     return jsonify({"message": "Item removed from cart successfully"})

# @app.route('/reviews', methods=['POST'])
# @jwt_required()
# def add_review():
#     user_id = get_jwt_identity()
#     data = request.json
#     new_review = Review(user_id=user_id, product_id=data['product_id'], rating=data['rating'], comment=data['comment'])
#     db.session.add(new_review)
#     db.session.commit()
#     return jsonify({"message": "Review added successfully", "id": new_review.id}), 201

# @app.route('/reviews/<int:review_id>', methods=['PUT'])
# @jwt_required()
# def update_review(review_id):
#     user_id = get_jwt_identity()
#     review = Review.query.filter_by(id=review_id, user_id=user_id).first_or_404()
#     data = request.json
#     review.rating = data.get('rating', review.rating)
#     review.comment = data.get('comment', review.comment)
#     db.session.commit()
#     return jsonify({"message": "Review updated successfully"})

# @app.route('/reviews/<int:review_id>', methods=['DELETE'])
# @jwt_required()
# def delete_review(review_id):
#     user_id = get_jwt_identity()
#     review = Review.query.filter_by(id=review_id, user_id=user_id).first_or_404()
#     db.session.delete(review)
#     db.session.commit()
#     return jsonify({"message": "Review deleted successfully"})

# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user_id = get_jwt_identity()
#     user = User.query.get(current_user_id)
#     return jsonify(id=user.id, username=user.username, email=user.email), 200

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)





# import logging
# from flask import Flask, request, jsonify
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from flask_migrate import Migrate
# from flask_cors import CORS
# from models import db, User, Product, CartItem, Review
# import os

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/ekart.db'
# app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')

# jwt = JWTManager(app)
# db.init_app(app)
# migrate = Migrate(app, db)
# CORS(app)

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.json
#     logger.debug(f"Register attempt with data: {data}")
#     user = User(username=data['username'], email=data['email'])
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     logger.info(f"User registered: {data['username']}")
#     return jsonify({"message": "User registered successfully"}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     logger.debug(f"Login attempt with data: {data}")
#     if not data:
#         logger.warning("Login attempt with no data")
#         return jsonify({"message": "No input data provided"}), 400
    
#     email = data.get('email')
#     password = data.get('password')
    
#     if not email or not password:
#         logger.warning("Login attempt with missing email or password")
#         return jsonify({"message": "Both email and password are required"}), 400
    
#     user = User.query.filter_by(email=email).first()
#     if user and user.check_password(password):
#         access_token = create_access_token(identity=user.id)
#         logger.info(f"Successful login for user: {email}")
#         return jsonify(access_token=access_token), 200
#     logger.warning(f"Failed login attempt for email: {email}")
#     return jsonify({"message": "Invalid credentials"}), 401


# @app.route('/products', methods=['GET'])
# def get_products():
#     logger.debug("Fetching all products")
#     products = Product.query.all()
#     return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products])

# @app.route('/products/<int:product_id>', methods=['GET'])
# def get_product(product_id):
#     logger.debug(f"Fetching product with id: {product_id}")
#     product = Product.query.get_or_404(product_id)
#     return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price})

# @app.route('/products', methods=['POST'])
# @jwt_required()
# def add_product():
#     data = request.json
#     logger.debug(f"Adding new product: {data}")
#     new_product = Product(name=data['name'], description=data['description'], price=data['price'])
#     db.session.add(new_product)
#     db.session.commit()
#     logger.info(f"New product added: {new_product.id}")
#     return jsonify({"message": "Product added successfully", "id": new_product.id}), 201

# @app.route('/products/<int:product_id>', methods=['PUT'])
# @jwt_required()
# def update_product(product_id):
#     logger.debug(f"Updating product with id: {product_id}")
#     product = Product.query.get_or_404(product_id)
#     data = request.json
#     product.name = data.get('name', product.name)
#     product.description = data.get('description', product.description)
#     product.price = data.get('price', product.price)
#     db.session.commit()
#     logger.info(f"Product updated: {product_id}")
#     return jsonify({"message": "Product updated successfully"})

# @app.route('/products/<int:product_id>', methods=['DELETE'])
# @jwt_required()
# def delete_product(product_id):
#     logger.debug(f"Deleting product with id: {product_id}")
#     product = Product.query.get_or_404(product_id)
#     db.session.delete(product)
#     db.session.commit()
#     logger.info(f"Product deleted: {product_id}")
#     return jsonify({"message": "Product deleted successfully"})

# @app.route('/cart', methods=['GET'])
# @jwt_required()
# def get_cart():
#     user_id = get_jwt_identity()
#     logger.debug(f"Fetching cart for user: {user_id}")
#     cart_items = CartItem.query.filter_by(user_id=user_id).all()
#     return jsonify([{"id": item.id, "product_id": item.product_id, "quantity": item.quantity} for item in cart_items])

# @app.route('/cart', methods=['POST'])
# @jwt_required()
# def add_to_cart():
#     user_id = get_jwt_identity()
#     data = request.json
#     logger.debug(f"Adding item to cart for user {user_id}: {data}")
#     cart_item = CartItem(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
#     db.session.add(cart_item)
#     db.session.commit()
#     logger.info(f"Item added to cart: {cart_item.id}")
#     return jsonify({"message": "Item added to cart successfully", "id": cart_item.id}), 201

# @app.route('/cart/<int:item_id>', methods=['DELETE'])
# @jwt_required()
# def remove_from_cart(item_id):
#     user_id = get_jwt_identity()
#     logger.debug(f"Removing item {item_id} from cart for user {user_id}")
#     cart_item = CartItem.query.filter_by(id=item_id, user_id=user_id).first_or_404()
#     db.session.delete(cart_item)
#     db.session.commit()
#     logger.info(f"Item removed from cart: {item_id}")
#     return jsonify({"message": "Item removed from cart successfully"})

# @app.route('/reviews', methods=['POST'])
# @jwt_required()
# def add_review():
#     user_id = get_jwt_identity()
#     data = request.json
#     logger.debug(f"Adding review for user {user_id}: {data}")
#     new_review = Review(user_id=user_id, product_id=data['product_id'], rating=data['rating'], comment=data['comment'])
#     db.session.add(new_review)
#     db.session.commit()
#     logger.info(f"Review added: {new_review.id}")
#     return jsonify({"message": "Review added successfully", "id": new_review.id}), 201

# @app.route('/reviews/<int:review_id>', methods=['PUT'])
# @jwt_required()
# def update_review(review_id):
#     user_id = get_jwt_identity()
#     logger.debug(f"Updating review {review_id} for user {user_id}")
#     review = Review.query.filter_by(id=review_id, user_id=user_id).first_or_404()
#     data = request.json
#     review.rating = data.get('rating', review.rating)
#     review.comment = data.get('comment', review.comment)
#     db.session.commit()
#     logger.info(f"Review updated: {review_id}")
#     return jsonify({"message": "Review updated successfully"})

# @app.route('/reviews/<int:review_id>', methods=['DELETE'])
# @jwt_required()
# def delete_review(review_id):
#     user_id = get_jwt_identity()
#     logger.debug(f"Deleting review {review_id} for user {user_id}")
#     review = Review.query.filter_by(id=review_id, user_id=user_id).first_or_404()
#     db.session.delete(review)
#     db.session.commit()
#     logger.info(f"Review deleted: {review_id}")
#     return jsonify({"message": "Review deleted successfully"})

# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user_id = get_jwt_identity()
#     logger.debug(f"Accessing protected route for user: {current_user_id}")
#     user = User.query.get(current_user_id)
#     return jsonify(id=user.id, username=user.username, email=user.email), 200

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)



import logging
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Product, CartItem, Review
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/ekart.db'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')

jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    logger.debug(f"Register attempt with data: {data}")
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    logger.info(f"User registered: {data['username']}")
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    logger.debug(f"Login attempt with data: {data}")
    if not data:
        logger.warning("Login attempt with no data")
        return jsonify({"message": "No input data provided"}), 400
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        logger.warning("Login attempt with missing email or password")
        return jsonify({"message": "Both email and password are required"}), 400
    
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        logger.info(f"Successful login for user: {email}")
        return jsonify(access_token=access_token), 200
    logger.warning(f"Failed login attempt for email: {email}")
    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/products', methods=['GET'])
def get_products():
    logger.debug("Fetching all products")
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    logger.debug(f"Fetching product with id: {product_id}")
    product = Product.query.get_or_404(product_id)
    return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price})

# @app.route('/products', methods=['POST'])
# @jwt_required()
# def add_product():
#     data = request.json
#     logger.debug(f"Adding new product: {data}")
#     new_product = Product(
#         name=data['name'],
#         description=data['description'],
#         price=data['price'],
#         image_url=data.get('image_url')  # Add this line
#     )
#     db.session.add(new_product)
#     db.session.commit()
#     logger.info(f"New product added: {new_product.id}")
#     return jsonify({"message": "Product added successfully", "id": new_product.id}), 201


@app.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    try:
        data = request.json
        logger.debug(f"Received data: {data}")
        if not data:
            return jsonify({"message": "No input data provided"}), 400

        # Validate required fields
        required_fields = ['name', 'price']
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"Missing required field: {field}"}), 422

        new_product = Product(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            image_url=data.get('image_url')
        )
        db.session.add(new_product)
        db.session.commit()
        logger.info(f"New product added: {new_product.id}")
        return jsonify({"message": "Product added successfully", "id": new_product.id}), 201

    except Exception as e:
        logger.error(f"Error adding product: {str(e)}")
        return jsonify({"message": "Error adding product", "error": str(e)}), 500





@app.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    logger.debug(f"Updating product with id: {product_id}")
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    db.session.commit()
    logger.info(f"Product updated: {product_id}")
    return jsonify({"message": "Product updated successfully"})

@app.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    logger.debug(f"Deleting product with id: {product_id}")
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    logger.info(f"Product deleted: {product_id}")
    return jsonify({"message": "Product deleted successfully"})

@app.route('/cart', methods=['GET'])
@jwt_required()
def get_cart():
    user_id = get_jwt_identity()
    logger.debug(f"Fetching cart for user: {user_id}")
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": item.id, "product_id": item.product_id, "quantity": item.quantity} for item in cart_items])

@app.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    data = request.json
    logger.debug(f"Adding item to cart for user {user_id}: {data}")
    cart_item = CartItem(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(cart_item)
    db.session.commit()
    logger.info(f"Item added to cart: {cart_item.id}")
    return jsonify({"message": "Item added to cart successfully", "id": cart_item.id}), 201

@app.route('/cart/<int:item_id>', methods=['DELETE'])
@jwt_required()
def remove_from_cart(item_id):
    user_id = get_jwt_identity()
    logger.debug(f"Removing item {item_id} from cart for user {user_id}")
    cart_item = CartItem.query.filter_by(id=item_id, user_id=user_id).first_or_404()
    db.session.delete(cart_item)
    db.session.commit()
    logger.info(f"Item removed from cart: {item_id}")
    return jsonify({"message": "Item removed from cart successfully"})

@app.route('/reviews', methods=['POST'])
@jwt_required()
def add_review():
    user_id = get_jwt_identity()
    data = request.json
    logger.debug(f"Adding review for user {user_id}: {data}")
    new_review = Review(user_id=user_id, product_id=data['product_id'], rating=data['rating'], comment=data['comment'])
    db.session.add(new_review)
    db.session.commit()
    logger.info(f"Review added: {new_review.id}")
    return jsonify({"message": "Review added successfully", "id": new_review.id}), 201

@app.route('/reviews/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    user_id = get_jwt_identity()
    logger.debug(f"Updating review {review_id} for user {user_id}")
    review = Review.query.filter_by(id=review_id, user_id=user_id).first_or_404()
    data = request.json
    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    db.session.commit()
    logger.info(f"Review updated: {review_id}")
    return jsonify({"message": "Review updated successfully"})

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    user_id = get_jwt_identity()
    logger.debug(f"Deleting review {review_id} for user {user_id}")
    review = Review.query.filter_by(id=review_id, user_id=user_id).first_or_404()
    db.session.delete(review)
    db.session.commit()
    logger.info(f"Review deleted: {review_id}")
    return jsonify({"message": "Review deleted successfully"})

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard_data():
    # Ensure only admin users can access this route
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({"message": "Access forbidden: Admins only"}), 403

    # Fetch dashboard data
    total_users = User.query.count()
    total_products = Product.query.count()
    total_reviews = Review.query.count()
    total_cart_items = CartItem.query.count()

    # Add more data as needed

    return jsonify({
        "total_users": total_users,
        "total_products": total_products,
        "total_reviews": total_reviews,
        "total_cart_items": total_cart_items,
    }), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    logger.debug(f"Accessing protected route for user: {current_user_id}")
    user = User.query.get(current_user_id)
    return jsonify(id=user.id, username=user.username, email=user.email), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
