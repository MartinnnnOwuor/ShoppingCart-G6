import logging
import os
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Product, CartItem, Review, Dashboard

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

# Route for user registration
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

# Route for user login
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

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    logger.debug("Fetching all products")
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products])

# Route to fetch a specific product by id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    logger.debug(f"Fetching product with id: {product_id}")
    product = Product.query.get_or_404(product_id)
    return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price})

# Route to fetch dashboard items
@app.route('/dashboard', methods=['GET'])
def get_dashboard_items():
    items = Dashboard.query.all()
    return jsonify([{'id': item.id, 'image_url': item.image_url, 'name': item.name} for item in items])

# Route to initialize dashboard with predefined images
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

# Route to add a new product
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

# Route to update an existing product
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

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    logger.debug(f"Deleting product with id: {product_id}")
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    logger.info(f"Product deleted: {product_id}")
    return jsonify({"message": "Product deleted successfully"})

# Route to fetch all items in the cart
@app.route('/cart', methods=['GET'])
@jwt_required()
def get_cart():
    user_id = get_jwt_identity()
    logger.debug(f"Fetching cart for user: {user_id}")
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": item.id, "product_id": item.product_id, "quantity": item.quantity} for item in cart_items])

# Route to add an item to the cart
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

# Route to remove an item from the cart
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

if __name__ == '__main__':
    app.run(debug=True)
