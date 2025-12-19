#  User Management System (Python + MySQL)

A console-based User Management Application built using **Python** and **MySQL**.  
This project allows users to **register, login, view profile details, and logout** through a clean, menu-driven interface.

The project is designed with proper **separation of concerns**, custom **exception handling**, and real-world **database interaction**.

## 🚀 Features

- User Registration with unique username validation
- Secure Login using username & password
- View user details after login
- Logout functionality
- Menu-driven console interface
- Custom exception handling
- Clean backend–frontend separation

## 🛠 Tech Stack

- **Python 3.x**
- **MySQL Community Server**
- **mysql-connector-python**

---

## 📂 Project Structure

user_management_project
- User_management_database.sql    (contains the database creation)
- app.py                           (Frontend menu & application flow)
- db_manager.py                   ( Database connection & queries)
- user.py                         (User model)
- exceptions.py                   (Custom exception classes)
- README.md

# Database Schema 
user_management_database.sql file contains the sql script of the database.

# ▶️ How to Run the Project

Clone the repository
```
git clone <repo-url>
cd user_management_project
```
Install dependency
```
pip install mysql-connector-python
```

Configure MySQL credentials in db_manager.py
Run the application
```
python app.py
```

#  What I Learned

- Designing a real-world console-based application
- Structuring Python projects using modular architecture
- Connecting Python with MySQL and performing CRUD operations
- Handling database cursors and buffered queries
- Implementing custom exception handling
- Managing application state (login/logout)
- Writing clean, readable, and maintainable code
