
import logging
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Product, CartItem, Review, Dashboard
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

@app.route('/api/dashboard')
def get_dashboard_items():
    items = Dashboard.query.all()
    return jsonify([
        {
            "id": item.id,
            "name": item.name,
            "image_url": item.image_url
        }
        for item in items
    ])

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

# @app.route('/dashboard', methods=['GET'])
# def get_dashboard_items():
#     items = Dashboard.query.all()
#     return jsonify([{'id': item.id, 'image_url': item.image_url, 'name': item.name} for item in items])

@app.route('/dashboard_images', methods=['GET'])
def get_dashboard_images():
    images = Dashboard.query.all()
    return jsonify([{'id': image.id, 'image_url': image.image_url, 'name': image.name} for image in images])


@app.route('/init_dashboard', methods=['POST'])
def init_dashboard():
    images = [
        {
            'image_url': 'https://images.unsplash.com/photo-1557825835-b4527f242af7?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fHRhYmxldHxlbnwwfHwwfHx8MA%3D%3D',
            'name': 'Tablets'
        },
        {
            'image_url': 'https://images.unsplash.com/photo-1605170439002-90845e8c0137?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHBob25lc3xlbnwwfHwwfHx8MA%3D%3D',
            'name': 'Phones'
        },
        {
            'image_url': 'https://images.unsplash.com/photo-1623126908029-58cb08a2b272?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fHRhYmxldHxlbnwwfHwwfHx8MA%3D%3D',
            'name': 'Phones'
        },
        {
            'image_url': 'https://images.unsplash.com/photo-1609252925148-b0f1b515e111?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fHBob25lc3xlbnwwfHwwfHx8MA%3D%3D',
            'name': 'Phones'
        }
    ]

    for img in images:
        new_image = Dashboard(image_url=img['image_url'], name=img['name'])
        db.session.add(new_image)
    db.session.commit()

    return jsonify({'message': 'Dashboard initialized with images'}), 201



@app.route('/dashboard', methods=['POST'])
@jwt_required()
def add_dashboard_item():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({"message": "Access forbidden: Admins only"}), 403

    data = request.json
    if not data or 'image_url' not in data or 'name' not in data:
        return jsonify({"message": "Invalid input. 'image_url' and 'name' are required."}), 400

    new_item = Dashboard(image_url=data['image_url'], name=data['name'])
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'Dashboard item added successfully', 'id': new_item.id}), 201

@app.route('/dashboard/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_dashboard_item(item_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({"message": "Access forbidden: Admins only"}), 403

    item = Dashboard.query.get_or_404(item_id)
    data = request.json
    item.image_url = data.get('image_url', item.image_url)
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify({"message": "Dashboard item updated successfully"})

@app.route('/dashboard/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_dashboard_item(item_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user.is_admin:
        return jsonify({"message": "Access forbidden: Admins only"}), 403

    item = Dashboard.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Dashboard item deleted successfully"})

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