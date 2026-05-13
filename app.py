from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hello@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)



order_product = db.Table(
    'order_product',

    db.Column(
        'order_id',
        db.Integer,
        db.ForeignKey('orders.id'),
        primary_key=True
    ),

    db.Column(
        'product_id',
        db.Integer,
        db.ForeignKey('products.id'),
        primary_key=True
    )
)

#classes for the database tables

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    orders = db.relationship('Order', backref='user', lazy=True)
    
    
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)

    order_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    products = db.relationship(
        'Product',
        secondary=order_product,
        backref='orders'
    )
    
class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True
        
class ProductSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Product
        load_instance = True
        
class OrderSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Order
        load_instance = True
        include_fk = True


#schema objects
user_schema = UserSchema()
users_schema = UserSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# User endpoints
@app.route('/users', methods=['GET'])
def get_users():

    all_users = User.query.all()

    return users_schema.jsonify(all_users)

#get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):

    user = User.query.get_or_404(id)

    return user_schema.jsonify(user)

#create a new user
@app.route('/users', methods=['POST'])
def create_user():

    data = request.json

    new_user = User(
        name=data['name'],
        address=data['address'],
        email=data['email']
    )

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

#update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):

    user = User.query.get(id)

    data = request.json

    user.name = data['name']
    user.address = data['address']
    user.email = data['email']

    db.session.commit()

    return user_schema.jsonify(user)

#delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):

    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})


#products endpoints
@app.route('/products', methods=['GET'])
def get_products():

    products = Product.query.all()

    return products_schema.jsonify(products)

#get product by id
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):

    product = Product.query.get(id)

    return product_schema.jsonify(product)

#create a new product
@app.route('/products', methods=['POST'])
def create_product():

    data = request.json

    product = Product(
        product_name=data['product_name'],
        price=data['price']
    )

    db.session.add(product)
    db.session.commit()

    return product_schema.jsonify(product)

#update a product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):

    product = Product.query.get(id)

    data = request.json

    product.product_name = data['product_name']
    product.price = data['price']

    db.session.commit()

    return product_schema.jsonify(product)

#delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"})

#order endpoints
@app.route('/orders', methods=['POST'])
def create_order():

    data = request.json

    order = Order(
        user_id=data['user_id']
    )

    db.session.add(order)
    db.session.commit()

    return order_schema.jsonify(order)

#add products to an order
@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):

    order = Order.query.get(order_id)
    product = Product.query.get(product_id)

    if product not in order.products:
        order.products.append(product)
        db.session.commit()

    return jsonify({"message": "Product added to order"})

#remove products from an order
@app.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product(order_id, product_id):

    order = Order.query.get(order_id)
    product = Product.query.get(product_id)

    if product in order.products:
        order.products.remove(product)
        db.session.commit()

    return jsonify({"message": "Product removed"})

#get order for user
@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):

    orders = Order.query.filter_by(user_id=user_id).all()

    return orders_schema.jsonify(orders)

#get products in an order
@app.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_for_order(order_id):

    order = Order.query.get(order_id)

    return products_schema.jsonify(order.products)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    

