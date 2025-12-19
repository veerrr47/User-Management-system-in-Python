from db_manager import register_user, login_user
from user import User
from exceptions import (
    UserAlreadyExistsError,
    InvalidCredentialsError,
    DatabaseError
)

# ---------------- MENU ---------------- #

def main_menu():
    print("\n+----------------------------------+")
    print("|       USER MANAGEMENT APP      |")
    print("+----------------------------------+")
    print("| 1. Login                         |")
    print("| 2. Register                      |")
    print("| 3. Exit                          |")
    print("+----------------------------------+")


def user_menu(user):
    print("\n+----------------------------------+")
    print(f"|      Welcome, {user['name']}!      |")
    print("+----------------------------------+")
    print(f"| ID       : {user['id']}")
    print(f"| Name     : {user['name']}")
    print(f"| Username : {user['username']}")
    print(f"| Address  : {user['address']}")
    print("+----------------------------------+")
    print("| 1. Logout                        |")
    print("+----------------------------------+")


# ---------------- HANDLERS ---------------- #

def handle_register():
    try:
        print("\n--- Register New User ---")
        name = input("Enter name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        address = input("Enter address: ")

        user = User(name, username, password, address)
        register_user(user)

        print("Registration successful! You can now login.")

    except UserAlreadyExistsError as e:
        print(f"❌ {e}")
    except DatabaseError as e:
        print(f"❌ {e}")


def handle_login():
    try:
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = login_user(username, password)
        print(" Login successful!")
        return user

    except InvalidCredentialsError as e:
        print(f"❌ {e}")
    except DatabaseError as e:
        print(f"❌ {e}")

    return None


# ---------------- MAIN APP LOOPS ---------------- #

def main():
    logged_in_user = None

    while True:
        if not logged_in_user:
            main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                logged_in_user = handle_login()
            elif choice == "2":
                handle_register()
            elif choice == "3":
                print("Exiting application!")
                break
            else:
                print(" Invalid choice. Try again.")

        else:
            user_menu(logged_in_user)
            choice = input("Enter your choice: ")

            if choice == "1":
                print(" Logged out successfully.")
                logged_in_user = None
            else:
                print("Invalid choice.")


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    main()
