# 🛒 CodeAlpha Simple E-Commerce Store

## Full Stack Development Internship Project

### Internship Organization

CodeAlpha

### Internship Domain

Full Stack Development

### Task

Task 1 – Simple E-Commerce Store

---

# Project Description

The Simple E-Commerce Store is a full-stack web application developed using Django. The project simulates a basic online shopping platform where users can browse products, view detailed product information, register accounts, log in securely, and manage products in a shopping cart.

The application demonstrates fundamental concepts of full-stack development including frontend design, backend development, database integration, user authentication, and dynamic content rendering.

This project was developed as part of the CodeAlpha Full Stack Development Internship to gain practical experience in building real-world web applications.

---

# Objectives

* Build a complete e-commerce web application.
* Implement user authentication and authorization.
* Store product and user data using a database.
* Create an interactive shopping experience.
* Understand Django MVC architecture.
* Learn CRUD operations and database management.
* Develop a project suitable for internship evaluation and portfolio presentation.

---

# Features Implemented

## Product Management

* Display available products.
* Product image display.
* Product pricing information.
* Product description display.
* Product detail page.

## User Management

* User Registration.
* User Login.
* Session Management.
* Authentication using Django Authentication System.

## Shopping Cart

* Add products to cart.
* View cart contents.
* Quantity management.
* Total price calculation.

## Database Integration

* SQLite database integration.
* Product storage.
* User storage.
* Cart storage.
* Order model implementation.

## Administrative Features

* Django Admin Panel.
* Product management through admin interface.
* User management through admin interface.
* Database monitoring.

---

# Technology Stack

## Frontend Technologies

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## Backend Technologies

* Python
* Django Framework

## Database

* SQLite3

## Development Tools

* VS Code
* Git
* GitHub
* Ubuntu Linux

---

# Software Requirements

* Python 3.10+
* Django 5/6
* Git
* Web Browser
* VS Code

---

# Project Architecture

```text
CodeAlpha_EcommerceStore
│
├── ecommerce
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
│
├── store
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations
│   └── tests.py
│
├── templates
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── orders.html
│   └── base.html
│
├── screenshots
│   ├── admin.png
│   ├── admin_administration.png
│   ├── login_page.png
│   ├── register_page.png
│   └── product_details.png
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# Database Models

## Product Model

Stores product information:

* Product Name
* Product Price
* Product Description
* Product Image

## Cart Model

Stores cart information:

* User
* Product
* Quantity

## Order Model

Stores order information:

* User
* Product
* Quantity
* Order Date

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/vu241fa04e14-ctrl/CodeAlpha_SimpleE-commerceStore.git
```

## Navigate to Project

```bash
cd CodeAlpha_EcommerceStore
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Admin User

```bash
python manage.py createsuperuser
```

## Run Application

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# Screenshots

## Registration Page

![Registration Page](screenshots/register_page.png)

## Login Page

![Login Page](screenshots/login_page.png)

## Product Details Page

![Product Details](screenshots/product_details.png)

## Admin Dashboard

![Admin Dashboard](screenshots/admin.png)

## Admin Management

![Admin Management](screenshots/admin_administration.png)

---

# Learning Outcomes

Through this project, the following concepts were learned:

* Django Framework
* MVC Architecture
* Database Management
* User Authentication
* URL Routing
* Template Rendering
* Bootstrap Integration
* Git Version Control
* GitHub Repository Management
* Full Stack Web Development

---

# Future Enhancements

* Product Search
* Product Categories
* Payment Gateway Integration
* Order Tracking
* Product Reviews
* Wishlist Functionality
* Responsive Mobile Design
* Email Notifications

---

# Author

Kedhar T

B.Tech – Computer Science and Engineering

Vignan University

---

# Internship Submission

CodeAlpha Full Stack Development Internship

Task 1: Simple E-Commerce Store
