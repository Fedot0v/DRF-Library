# Library Management API

This project is a Library Management System built with Django REST Framework. It provides core services for managing books, users, and borrowings, including user authentication, book lending, return tracking, and notifications via a Telegram bot.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Database Schema](#database-schema)
- [Installation Instructions](#installation-instructions)
- [API Documentation](#api-documentation)

## Technologies Used
- **Python**: Core language
- **Django**: Backend framework
- **Django REST Framework**: API building
- **Stripe**: Payment processing
- **Telegram Bot API**: Sends notifications

## Features
- **User Authentication**: Secure login and registration
- **Book Management**: Create, update, delete, and view books
- **Borrowing System**: Borrow and return books
- **Payment Processing**: Integrates with Stripe
- **Telegram Notifications**: Alerts about borrowings via a Telegram bot

## Database Schema
![LibraryAPI.png](LibraryAPI.png)

## Installation instruction
**Clone repository**:
```bash
    git clone git@github.com:Fedot0v/DRF-Library.git
    cd DRF-Library
   ```
**Set Up Environment Variables**:
- Create a .env file based on the env.sample, with values for Stripe, Telegram bot token, and other settings.

**Install Dependencies**:
```bash
pip install -r requirements.txt
```
**Run Database Migrations**:
```bash
python manage.py migrate
```

**Start the Development Server**:
```bash
python manage.py runserver
```

## API Documentation
API documentation is generated using **drf-spectacular**. To access the Swagger UI, visit `http://localhost:8000/api/schema/swagger-ui/`, and for the OpenAPI schema in JSON format, visit `http://localhost:8000/api/schema/`.

- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/`
- **OpenAPI JSON**: `http://localhost:8000/api/schema/`