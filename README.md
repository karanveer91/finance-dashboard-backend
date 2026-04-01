# Finance Data Processing and Access Control Backend

## Overview

This project is a backend system designed for a finance dashboard application.
It provides APIs for managing users, handling financial records, and generating summary analytics for a dashboard.

The backend demonstrates core backend development concepts such as API design, data modeling, role-based access control, and structured data processing.

The system is built using **Python** and **FastAPI**, with **SQLite** used as the database for data persistence.

---

## Objectives

The goal of this project is to demonstrate backend engineering skills including:

* API development
* Database modeling
* Business logic implementation
* Role-based access control
* Data validation and error handling
* Backend architecture organization

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

---

## Features

### 1. User Management

The backend supports basic user management functionality including:

* Creating users
* Assigning roles
* Managing user status

Supported roles include:

* **Viewer** – Can view dashboard data only
* **Analyst** – Can view records and analytics
* **Admin** – Can create, update, and manage records and users

---

### 2. Financial Records Management

The system allows users to manage financial records.

Each record includes:

* Amount
* Type (Income or Expense)
* Category
* Date
* Notes / Description

Supported operations:

* Create records
* View records
* Update records
* Delete records
* Filter records

---

### 3. Dashboard Summary APIs

The backend provides APIs to generate aggregated financial data for dashboards.

Examples include:

* Total Income
* Total Expenses
* Net Balance
* Financial overview based on records

These APIs demonstrate backend logic for calculating aggregated financial insights.

---

### 4. Access Control

Role-based access control is implemented to restrict actions based on user roles.

Example rules:

* Viewers cannot modify records
* Analysts can view records and summaries
* Admins can create and manage records and users

---

### 5. Data Validation and Error Handling

The backend ensures that:

* Invalid inputs are validated
* Proper error responses are returned
* HTTP status codes are used appropriately

---

## Project Structure

```
finance_backend
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── roles.py
└── requirements.txt
```

### File Description

**main.py**
Contains the main FastAPI application and API endpoints.

**database.py**
Handles database configuration and connection.

**models.py**
Defines database tables using SQLAlchemy.

**schemas.py**
Defines request and response models using Pydantic.

**auth.py**
Contains authentication logic and token generation.

**roles.py**
Implements role-based access control.

**requirements.txt**
Lists all project dependencies.

---

## Installation and Setup

### 1. Clone the repository

```
git clone <repository-link>
```

### 2. Navigate to the project folder

```
cd finance_backend
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the server

```
uvicorn main:app --reload
```

---

## API Documentation

After starting the server, open:
```
#paste in terminal:-

source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

```

```
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation using Swagger UI.

---

## Example API Endpoints

Create user

```
POST /users
```

Create financial record

```
POST /records
```

Get all records

```
GET /records
```

Dashboard summary

```
GET /dashboard
```

---

## Assumptions

* SQLite is used for simplicity and local development.
* Authentication is simplified for demonstration purposes.
* The system is designed for backend evaluation rather than production deployment.

---

## Possible Future Improvements

* JWT authentication
* Pagination for record lists
* Search and filtering support
* Advanced analytics APIs
* Unit testing
* Production database integration

---

## Conclusion

This project demonstrates a structured backend system that handles financial data, user roles, and dashboard analytics.
The implementation focuses on clean architecture, clear API design, and maintainable backend logic.
