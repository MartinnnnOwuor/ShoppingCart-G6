e-Kart: Your Ultimate Online Shopping Experience

Overview
e-Kart is a dynamic and innovative e-commerce platform designed to revolutionize the online shopping experience. 
Leveraging the power of React for the front-end and Flask for the back-end, e-Kart offers a seamless, fast, and intuitive interface for both shoppers and sellers.
Whether you're a small business owner looking to expand your reach or a consumer searching for the best deals, e-Kart is your go-to solution.

Key Features

User-Friendly Interface:
A sleek and responsive design built with React ensures a smooth shopping experience on any device.
Intuitive navigation and a visually appealing layout make it easy for users to find what they're looking for.

Robust Back-End:
Powered by Flask, the back-end ensures secure, efficient, and scalable performance.
Seamless integration with databases for reliable data management.

Advanced Shopping Cart:
Add, remove, and update items with ease.
Real-time cart updates and an efficient checkout process.

Technologies Used

Front-End
React: For building the user interface.
React Router: For routing.
Axios: For making HTTP requests.
Material-UI: For styling components.

Back-End
Flask: For building the web server.
Flask-RESTful: For creating RESTful APIs.
SQLAlchemy: For database management.
Marshmallow: For object serialization and deserialization.
JWT (JSON Web Tokens): For authentication.

Installation Pre-requisites and Steps

Steps
Clone the repository:

'''
git clone https://github.com/yourusername/e-kart.git
cd e-kart
'''

Set up the back-end:

cd server
source venv/bin/activate
pip install Flask==2.2.5 Flask-SQLAlchemy==2.5.1 SQLAlchemy==1.4.46 Flask-JWT-Extended==4.4.0 Flask-Migrate==3.1.0 Flask-CORS==3.0.10 Werkzeug==2.2.3 python-dotenv==0.19.0
flask run

Set up the front-end:

cd ../client
npm install && npm start


Configure environment variables:

Create a .env file in the backend directory with the following content:

DATABASE_URI=sqlite://username:password@localhost/e_kart
SECRET_KEY=your_secret_key

Run the application:

Back-end:

cd server
flask run/ python3 app.py

Front-end:

cd ../client
npm start

Access the application:

Front-end: http://localhost:3000
Back-end: http://localhost:5000


Usage

Front-End
Navigate through the product listings.
Add items to the cart.
Proceed to checkout and complete the purchase.

Back-End
API endpoints for managing products, users, and orders.
Authentication and authorization mechanisms.

API Endpoints
User Endpoints
POST /register: Register a new user.
POST /login: Login an existing user.

Product Endpoints
GET /products: Get all products.
GET /products/<id>: Get a specific product.
POST /products: Add a new product (admin).
PUT /products/<id>: Update a product (admin).
DELETE /products/<id>: Delete a product (admin).


