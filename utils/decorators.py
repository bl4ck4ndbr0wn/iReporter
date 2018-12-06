from functools import wraps

from flask import request, abort

from app.api.v2.models.user import User


def jwt_required(f):
    """
    restrict access if not authorized

    :param f:
    :return: True
    """
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        auth_header = None
        if 'Authorization' in request.headers:
            auth_header = request.headers.get('Authorization')
            access_token = auth_header.split(" ")[1]
            if access_token:
                # Attempt to decode the token and get the User ID
                user_id = User().decode_token(access_token)
                if not isinstance(user_id, str):
                    # Go ahead and handle the request, the user is authenticated
                    user = User().find_by_id(user_id)
                    if user:
                        return f(*args, **kwargs)
                    return {'message': 'User not found.'}, 401
        else:
            return {'message': 'Authorization header is missing in this request.'}, 403
    return wrapper_function
