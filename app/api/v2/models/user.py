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

    @staticmethod
    def generate_token(user_id):
        """
        Encoding user id to get JSON Web Tokens (JWT)

        :param user_id: Int
        :return: token
        """
        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=15),  # Expiration Time
                'iat': datetime.utcnow(),  # Issued At
                'user_id': user_id  # payload
            }
            # create the byte string token using the payload and the SECRET key
            encoded_jwt = jwt.encode(
                payload,
                current_app.config.get('JWT_SECRET_KEY'),
                algorithm='HS512'
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
                                 algorithms=['HS512', 'HS256'])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            # Raised when a token’s exp claim indicates that it has expired
            return {
                "status": 401,
                "message": "Expired token. Please login to get a new token"
            }, 401
        except jwt.InvalidSignatureError:
            # Raised when a token’s signature doesn’t match
            # the one provided as part of the token.
            return {
                       "status": 422,
                       "message": "Invalid token. Please login"
                   }, 422
        except jwt.InvalidTokenError:
            # Base exception when decode() fails on a token
            return {
                "status": 422,
                "message": "Invalid token. Please login"
            }, 422

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
