# MyStore — Full Stack E-Commerce Application

A full-stack e-commerce web application built with Django REST Framework and vanilla JavaScript, featuring user authentication, product management, shopping cart, and order processing.

🌐 **Live Demo:** [https://snazzy-figolla-757755.netlify.app](https://snazzy-figolla-757755.netlify.app)  
🔗 **API Base URL:** [https://my-store-vaa0.onrender.com/api](https://my-store-vaa0.onrender.com/api)

---

## Features

- Browse and search products
- User registration and login with JWT authentication
- Product detail page with quantity selector
- Shopping cart with localStorage persistence
- Order placement and order history
- Django admin panel for managing products, orders, and users
- Fully deployed on Render (backend) and Netlify (frontend)

---

## Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| Django 6.0 | Web framework |
| Django REST Framework | REST API |
| djangorestframework-simplejwt | JWT authentication |
| django-cors-headers | CORS handling |
| Gunicorn | Production WSGI server |
| WhiteNoise | Static file serving |
| SQLite | Database (development & production) |

### Frontend
| Technology | Purpose |
|---|---|
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript (ES6+) | Interactivity & API calls |
| localStorage | Cart persistence |

### Deployment
| Service | Purpose |
|---|---|
| Render | Backend hosting |
| Netlify | Frontend hosting |
| GitHub | Version control |

---

## Project Structure

```
my_store/
├── my_store/                  ← Django project root
│   ├── core/                  ← Project config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── store/                 ← Main app
│   │   ├── models.py          ← Product, Order, OrderItem
│   │   ├── views.py           ← API views
│   │   ├── serializers.py     ← DRF serializers
│   │   ├── urls.py            ← App URL patterns
│   │   └── admin.py           ← Admin registration
│   ├── frontend/              ← Static frontend
│   │   ├── index.html         ← Product listing
│   │   ├── product.html       ← Product detail
│   │   ├── cart.html          ← Shopping cart
│   │   ├── login.html         ← Login page
│   │   ├── register.html      ← Register page
│   │   ├── orders.html        ← Order history
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       ├── api.js         ← API calls
│   │       ├── auth.js        ← Auth logic
│   │       └── cart.js        ← Cart logic
│   ├── manage.py
│   └── requirements.txt
```

---

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/products/` | List all products | No |
| GET | `/api/products/?search=x` | Search products | No |
| GET | `/api/products/:id/` | Product detail | No |
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Login & get JWT token | No |
| POST | `/api/auth/refresh/` | Refresh JWT token | No |
| GET | `/api/auth/profile/` | Get logged-in user | Yes |
| GET | `/api/orders/` | List user's orders | Yes |
| POST | `/api/orders/` | Place new order | Yes |
| GET | `/api/orders/:id/` | Order detail | Yes |

---

## Database Schema

```
Users (Django built-in)
├── id, username, email, password_hash

Products
├── id, name, description, price, stock_quantity, image_url, created_at

Orders
├── id, user_id (FK), status, total_price, created_at

OrderItems
├── id, order_id (FK), product_id (FK), quantity, unit_price
```

---

## Local Setup

### Prerequisites
- Python 3.10+
- Git

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/samiera12/my_store.git
cd my_store/my_store
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Create superuser**
```bash
python manage.py createsuperuser
```

**6. Start the development server**
```bash
python manage.py runserver
```

**7. Open the frontend**

Open `frontend/index.html` in your browser, or use VS Code Live Server.

> Make sure `BASE_URL` in `frontend/js/api.js` points to `http://127.0.0.1:8000/api` for local development.

---

## Deployment

### Backend — Render
- **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command:** `gunicorn core.wsgi:application --bind 0.0.0.0:$PORT`
- **Root Directory:** `my_store`
- **Environment Variables:** `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `PYTHON_VERSION=3.11`

### Frontend — Netlify
- Drag and drop the `frontend/` folder onto Netlify's manual deploy area
- Update `BASE_URL` in `js/api.js` to point to your Render backend URL

---





## License

This project is open source and available under the [MIT License](LICENSE).
