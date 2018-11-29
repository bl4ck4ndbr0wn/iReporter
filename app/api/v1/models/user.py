from werkzeug.security import generate_password_hash, check_password_hash


user_table = []


class User:
    """
    User model.

    initializing user primary_key
    """
    id = 1

    def __init__(self,
                 username=None,
                 password=None,
                 firstname=None,
                 lastname=None,
                 othername=None,
                 email=None,
                 phonenumber=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phonenumber
        self.username = username
        self.password = User.encrypt_password(password)

        User.id += 1

    def __repr__(self):
        """ Return repr(self). """
        return "{} in User Model.".format(self.username)

    @staticmethod
    def find_by_name(username):
        """
        Find a user by their username.

        :param username: username
        :type username: str
        :return: User instance
        """
        for user in user_table:
            if user.username == username:
                return user
        return None

    @staticmethod
    def find_by_id(user_id):
        """
        Find a user by their id.

        :param user_id: username
        :type user_id: int
        :return: User instance
        """
        for user in user_table:
            if user.id == user_id:
                return user
        return None

    @classmethod
    def encrypt_password(cls, plaintext_password):
        """
        Hash a plaintext string using PBKDF2. This is good enough according
        to the NIST (National Institute of Standards and Technology).

        :param plaintext_password: Password in plain text
        :type plaintext_password: str
        :return: str
        """
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    def authenticated(self, password=''):
        """
        Ensure a user is authenticated, and optionally check their password.

        :param password: Optionally verify this as their password
        :type password: str
        :return: bool
        """
        return check_password_hash(self.password, password)

    def save_to_db(self):
        user_table.append(self)
