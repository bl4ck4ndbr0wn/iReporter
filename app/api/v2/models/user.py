from werkzeug.security import generate_password_hash, check_password_hash
from instance.db import Model


class User(Model):
    """
    User model.
    """

    def __init__(self,
                 email=None,
                 username=None,
                 password=None,
                 firstname=None,
                 lastname=None,
                 othername=None,
                 phonenumber=None,
                 is_admin=False):
        super().__init__()
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phonenumber
        self.username = username
        self.password = User.encrypt_password(password)
        self.is_admin = is_admin

    def __repr__(self):
        """ Return repr(self). """
        return "{} in User Model.".format(self.username)

    def find_by_name(self, username):
        """
        Find a user by their username.

        :param username: username
        :type username: str
        :return: User instance
        """
        self.cursor.execute("SELECT * FROM users "
                            "WHERE username=%s", (username,))
        user = self.fetch_one()

        if user:
            return user
        return None

    def find_by_id(self, user_id):
        """
        Find a user by their id.

        :param user_id: username
        :type user_id: int
        :return: User instance
        """
        self.cursor.execute("SELECT * FROM users "
                            "WHERE id=%s", (user_id,))
        user = self.fetch_one()

        if user:
            return user
        return None

    @staticmethod
    def encrypt_password(plaintext_password):
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
        query = "INSERT INTO users (username, password, firstname, " \
                "lastname, phonenumber, email, othernames, is_admin) " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"  # Note: no quotes
        data = (self.username, self.password,
                self.firstname, self.lastname,
                self.phoneNumber, self.email,
                self.othername, self.is_admin,)

        self.cursor.execute(query, data)
        self.save()

    def map_user(self, data):
        """ map user to user object"""
        self.id = data["id"]
        self.firstname = data["firstname"]
        self.lastname = data["lastname"]
        self.othername = data["othername"]
        self.email = data["email"]
        self.phoneNumber = data["phonenumber"]
        self.username = data["username"]
        self.password = data["password"]
        self.is_admin = data["is_admin"]

