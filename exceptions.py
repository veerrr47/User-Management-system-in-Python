class UserError(Exception):
    pass
    """"Base class for user errors """

class UserAlreadyExistsError(UserError):
    pass
    """"This error is raised when user is trying to use the username that already exists """

class InvalidCredentialsError(UserError):
    pass
    """"This error is raised when login credentials are incorrect """

class DatabaseError(UserError):
    pass
    """"This error is raised when database operation fails """