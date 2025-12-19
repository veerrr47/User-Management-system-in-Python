class User:
    def __init__(self, name, username, password, address):
        self.name = name
        self.username = username
        self.password = password
        self.address = address


    def to_dict(self):
        return {
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "address": self.address

        }
        """This will convert the user which is in object into a dictonary, it'll come in handy while interacting with the database """