# E-commerce API with Flask

A comprehensive full-stack e-commerce API built with Flask, featuring a complete relational database design and RESTful API endpoints for managing products, orders, and users.

## Project Overview

This final project combines relational database design with API development to create a production-ready e-commerce backend. It demonstrates advanced concepts in database architecture, RESTful API design, authentication, and Flask framework implementation.

## Tech Stack

- **Python** - 97.7%
- **C++** - 1.6%
- **C** - 0.4%
- **PowerShell** - 0.1%
- **Cython** - 0.1%
- **JavaScript** - 0.1%

### Key Technologies

- **Flask** - Python web framework
- **SQLAlchemy** - ORM and database management
- **PostgreSQL/MySQL** - Relational database
- **Flask-RESTful** - REST API extension
- **Flask-JWT-Extended** - Authentication and authorization
- **Marshmallow** - Data serialization and validation
- **Gunicorn** - WSGI application server

## Features

### Core Functionality
- 🛍️ Product management (CRUD operations)
- 🛒 Shopping cart system
- 📦 Order management
- 👥 User authentication and authorization
- 💳 Payment processing integration
- 📊 Admin dashboard and analytics
- 🔍 Advanced search and filtering
- 📧 Email notifications

### Technical Features
- 🔐 JWT authentication
- 📝 Comprehensive API documentation
- 🧪 Unit and integration tests
- 📊 Database logging and monitoring
- ⚡ Performance optimization
- 🔄 Database migrations
- 💾 Data validation and serialization

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher (or MySQL)
- pip and virtualenv
- Postman or similar API testing tool (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/prellwitzdarian/Relational-Databases-and-API-Final-Project.git
cd Relational-Databases-and-API-Final-Project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Initialize the database:
```bash
python create_db.py
# or using Alembic migrations:
alembic upgrade head
```

6. Run the development server:
```bash
python app.py
# or
flask run
```

The API will be available at `http://localhost:5000`

## Project Structure

```
Relational-Databases-and-API-Final-Project/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── order_item.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── orders.py
│   │   └── users.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   └── order_schema.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── helpers.py
│   └── database.py
├── migrations/
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_products.py
│   └── test_orders.py
├── config.py
├── requirements.txt
├── .env.example
├── create_db.py
├── app.py
├── README.md
└── .gitignore
```

## Database Schema

### Users Table
```
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- first_name
- last_name
- created_at
- updated_at
```

### Products Table
```
- id (Primary Key)
- name
- description
- price
- stock_quantity
- category_id (Foreign Key)
- created_at
- updated_at
```

### Orders Table
```
- id (Primary Key)
- user_id (Foreign Key)
- order_date
- total_amount
- status
- shipping_address
- created_at
- updated_at
```

### OrderItems Table
```
- id (Primary Key)
- order_id (Foreign Key)
- product_id (Foreign Key)
- quantity
- unit_price
- created_at
```

### Categories Table
```
- id (Primary Key)
- name
- description
- created_at
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh JWT token

### Products
- `GET /api/products` - Get all products
- `GET /api/products/<id>` - Get product by ID
- `POST /api/products` - Create product (Admin)
- `PUT /api/products/<id>` - Update product (Admin)
- `DELETE /api/products/<id>` - Delete product (Admin)
- `GET /api/products/search?q=<query>` - Search products

### Orders
- `GET /api/orders` - Get user's orders
- `GET /api/orders/<id>` - Get order details
- `POST /api/orders` - Create new order
- `PUT /api/orders/<id>` - Update order
- `DELETE /api/orders/<id>` - Cancel order

### Users
- `GET /api/users/<id>` - Get user profile
- `PUT /api/users/<id>` - Update user profile
- `GET /api/users/<id>/orders` - Get user's orders

## Authentication

JWT (JSON Web Tokens) is used for authentication:

1. User logs in with credentials
2. Server returns JWT token
3. Include token in Authorization header: `Bearer <token>`
4. Server validates token on protected routes

## Running Tests

```bash
pytest
# With coverage:
pytest --cov=app tests/

# Specific test file:
pytest tests/test_auth.py

# Verbose output:
pytest -v
```

## Configuration

Create a `.env` file based on `.env.example`:

```env
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=postgresql://user:password@localhost/ecommerce_db
JWT_SECRET_KEY=your-secret-key-here
JWT_ACCESS_TOKEN_EXPIRES=3600
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-password
```

## Deployment

### Using Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]
```

### Cloud Deployment Options
- AWS Elastic Beanstalk
- Google Cloud App Engine
- Heroku
- DigitalOcean
- Azure App Service

## Learning Outcomes

This project demonstrates proficiency in:
- Flask framework and best practices
- RESTful API design and implementation
- Relational database design
- SQLAlchemy ORM usage
- Authentication and authorization (JWT)
- Data validation and serialization
- Unit and integration testing
- Error handling and logging
- API documentation
- Database optimization
- Code organization and patterns
- Deployment and DevOps basics

## API Documentation

Comprehensive API documentation available at:
- Swagger UI: `http://localhost:5000/api/docs`
- ReDoc: `http://localhost:5000/api/redoc`

## Error Handling

The API returns standardized error responses:

```json
{
  "error": "Error message",
  "status": 400,
  "timestamp": "2026-05-13T10:30:00Z"
}
```

## Security Considerations

- ✅ Password hashing with bcrypt
- ✅ JWT token validation
- ✅ CORS configuration
- ✅ SQL injection prevention via SQLAlchemy
- ✅ Rate limiting (optional)
- ✅ Input validation and sanitization
- ✅ HTTPS enforcement (production)

## Performance Optimization

- Database indexing on frequently queried columns
- Pagination for large datasets
- Caching strategies
- Query optimization
- Connection pooling

## Troubleshooting

### Database Connection Error
- Verify PostgreSQL is running
- Check DATABASE_URL format
- Verify credentials in .env file

### JWT Token Issues
- Ensure JWT_SECRET_KEY is set
- Check token expiration
- Verify Authorization header format

### Port Already in Use
```bash
# Find and kill process on port 5000
lsof -i :5000  # macOS/Linux
# netstat -ano | findstr :5000  # Windows
```

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-RESTful Extension](https://flask-restful.readthedocs.io/)
- [JWT Documentation](https://tools.ietf.org/html/rfc7519)

## Future Enhancements

- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Email notification system
- [ ] Advanced analytics dashboard
- [ ] Inventory management system
- [ ] Customer reviews and ratings
- [ ] Coupon and discount system
- [ ] Multi-language support
- [ ] GraphQL API alternative
- [ ] WebSocket support for real-time updates
- [ ] Mobile app backend

## License

This project is provided as-is for educational purposes.

## Author

Created by Darian Prellwitz

---

**Last Updated:** May 2026
