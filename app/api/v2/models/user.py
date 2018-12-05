from werkzeug.security import generate_password_hash, check_password_hash
from instance.db import Model


class User(Model):
    """
    User model.
    """

    def __init__(self,
                 is_admin,
                 email,
                 username,
                 password,
                 firstname,
                 lastname,
                 othername="",
                 phonenumber=0):
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

    def find_by_name(self):
        """
        Find a user by their username.

        :param username: username
        :type username: str
        :return: User instance
        """
        self.cursor.execute("SELECT * FROM users "
                            "WHERE username=%s", (self.username,))
        user = self.fetch_one()

        if user:
            return user
        return None

    def find_by_id(self):
        """
        Find a user by their id.

        :param user_id: username
        :type user_id: int
        :return: User instance
        """
        query = f"SELECT * FROM users WHERE id={self.id}"
        self.query(query)
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
