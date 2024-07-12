from flask import Blueprint, request, jsonify
from .models import User, Product, Order
from . import db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@main.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 200

@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products])

@main.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    products = Product.query.filter(Product.nameOfProduct.contains(query)).all()
    return jsonify([product.as_dict() for product in products])

@main.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.as_dict())

@main.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.get_json()
    new_product = Product(
        nameOfProduct=data['nameOfProduct'],
        price=data['price'],
        imageUrl=data['imageUrl'],
        quantity=data['quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

@main.route('/order', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_order = Order(
        user_id=user_id,
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

# Helper function to convert model instances to dictionaries
def to_dict(instance):
    return {c.name: getattr(instance, c.name) for c in instance.__table__.columns}

Product.as_dict = to_dict
