# Flask Authentication & Authorization App

## Overview
This is a Flask-based web application that implements **authentication (login/logout)** and **authorization (access control)** using **PostgreSQL, Flask-Session, and password hashing**. It ensures that only authenticated users can access restricted pages.

## Features
- **User Registration** (Secure password hashing using bcrypt)
- **User Login & Logout** (Session-based authentication)
- **Access Control** (Restrict unauthorized access using decorators)
- **Flash Messages** for real-time feedback

## Installation & Setup

### 1. Install Dependencies
Install the required Python libraries to run the application.

### 2. Set Up PostgreSQL Database
Create a PostgreSQL database and update the configuration settings in the application.

### 3. Run the Application
Run the Flask application and access it through a web browser.

## Authentication & Authorization Implementation

### 1️⃣ User Registration
- Users enter a username and password.
- Passwords are hashed before storing in PostgreSQL.
- Existing usernames are checked to prevent duplicates.

### 2️⃣ User Login
- User credentials are verified.
- Passwords are validated using bcrypt.
- A session is created to maintain the login state.

### 3️⃣ Protecting Routes (Authorization)
- The application restricts unauthorized access using a login-required mechanism.
- If a user is not logged in, they are redirected to the login page.

### 4️⃣ Logout Functionality
- Clears the user session to log out the user and redirect them to the homepage.

## Summary
✅ Secure password storage using hashing  
✅ Session-based authentication to track logged-in users  
✅ Access control via decorators to protect restricted pages  
✅ Flash messages for real-time feedback  

## Future Enhancements
- Implement JWT-based authentication
- Add OAuth (Google/Facebook Login)
- Enable email verification for new users

---
This project provides a **secure and beginner-friendly** implementation of authentication and authorization in Flask. 🚀

