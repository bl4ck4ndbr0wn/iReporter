import jwt
from datetime import datetime, timedelta
from flask import current_app
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
                 othernames=None,
                 lastname=None,
                 phonenumber=None,
                 is_admin=False):
        super().__init__()
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phonenumber = phonenumber
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
        self.save()

        if user:
            return self.map_user(user)
        return None

    def find_by_id(self, user_id):
        """
        Find a user by their id.

        :param user_id: user_id
        :type user_id: int
        :return: User instance
        """
        self.cursor.execute("SELECT * FROM users "
                            "WHERE id=%s", (user_id,))
        user = self.fetch_one()
        self.save()

        if user:
            return self.map_user(user)
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

    def authenticated(self, password):
        """
        Ensure a user is authenticated, and optionally check their password.

        :param password: Optionally verify this as their password
        :type password: str
        :return: bool
        """
        return check_password_hash(self.password, password)

    def generate_token(self):
        """
        Encoding user id to get JSON Web Tokens (JWT)

        :return: token
        """
        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=15),  # Expiration Time
                'iat': datetime.utcnow(),  # Issued At
                'user_id': self.id  # payload
            }
            # create the byte string token using the payload and the SECRET key
            encoded_jwt = jwt.encode(
                payload,
                current_app.config.get('JWT_SECRET_KEY'),
                algorithm='HS256'
            )
            return encoded_jwt
        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    @staticmethod
    def decode_token(token):
        """
        Decodes the access token from the Authorization header.

        :param token: String
        :return: Payload
        """
        try:
            payload = jwt.decode(token,
                                 current_app.config.get('JWT_SECRET_KEY'),
                                 algorithms=['HS256'])
            return payload["user_id"]
        except jwt.DecodeError:
            # Raised when a token cannot be decoded because it failed validation
            return "Token failed validation hence decode failed."
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"

    def blacklist_token(self, token):
        """
        Blacklist already expired token or invalid.
        :param token:
        :return: None.
        """
        query = "INSERT INTO token (token) VALUES(%s);"
        data = (token,)
        self.cursor.execute(query, data)
        self.save()

    def save_to_db(self):
        query = "INSERT INTO users (username, password, firstname, " \
                "lastname, phonenumber, email, othernames, is_admin) " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"  # Note: no quotes
        data = (self.username, self.password,
                self.firstname, self.lastname,
                self.phonenumber, self.email,
                self.othernames, self.is_admin,)

        self.cursor.execute(query, data)
        self.save()

    def update_user(self, data):
        query = "UPDATE users SET firstname = %s, lastname = %s, " \
                "phonenumber = %s, email = %s , othernames = %s " \
                "WHERE id = %s;"  # Note: no quotes
        data = (data.firstname, data.lastname,
                data.phonenumber, data.email,
                data.othernames, self.id,)
        self.cursor.execute(query, data)
        self.save()

    def map_user(self, data):
        """ map user to user object"""
        self.id = data[0]
        self.username = data[1]
        self.password = data[2]
        self.firstname = data[3]
        self.lastname = data[4]
        self.othernames = data[5]
        self.email = data[6]
        self.phonenumber = data[7]
        self.is_admin = data[8]

        return self
