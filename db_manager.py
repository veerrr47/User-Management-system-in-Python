import mysql.connector
from user import User
from exceptions import (
    DatabaseError,
    UserAlreadyExistsError,
    InvalidCredentialsError
)


# ---------------- DATABASE CONNECTION ---------------- #

def get_connection():
    """Creates and returns a MySQL database connection"""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="user_management"
        )
    except mysql.connector.Error:
        raise DatabaseError("Failed to connect to the database")


# ---------------- REGISTER USER ---------------- #

def register_user(user: User):
    """ This will Register a new user in the database"""
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(buffered=True)

        # This will Check if username already exists
        cursor.execute(
            "SELECT id FROM users WHERE username = %s",
            (user.username,)
        )

        if cursor.fetchone():
            raise UserAlreadyExistsError("Username already exists")

        # Insert user
        cursor.execute(
            """
            INSERT INTO users (name, username, password, address)
            VALUES (%s, %s, %s, %s)
            """,
            (user.name, user.username, user.password, user.address)
        )

        conn.commit()

    except UserAlreadyExistsError:
        raise
    except Exception as e:
        raise DatabaseError(f"Error while registering user: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# ---------------- LOGIN USER ---------------- #

def login_user(username: str, password: str):
    """This will authenticate user using username and password"""
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(buffered=True)

        cursor.execute(
            """
            SELECT id, name, username, address
            FROM users
            WHERE username = %s AND password = %s
            """,
            (username, password)
        )

        result = cursor.fetchone()

        if not result:
            raise InvalidCredentialsError("Invalid username or password")

        return {
            "id": result[0],
            "name": result[1],
            "username": result[2],
            "address": result[3]
        }

    except InvalidCredentialsError:
        raise
    except Exception as e:
        raise DatabaseError(f"Login failed: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
