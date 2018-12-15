from functools import wraps
import json
from flask import request, Response, g

from app.api.v2.models.user import User


def decode_token(access_token):
    """
    Attempt to decode the token and get the User ID
    :param access_token:
    :return: user_id
    """
    if access_token:
        user_id = User().decode_token(access_token)
        if not isinstance(user_id, str):
            # Go ahead and handle the request, the user is authenticated
            return user_id
        else:
            User().blacklist_token(access_token)
            return user_id
    else:
        return Response(
            mimetype="application/json",
            response=json.dumps({'status': 400,
                                 'error': 'Authentication token is '
                                          'not available, please login '
                                          'to get one'}),
            status=400
        )


def jwt_required(f):
    """
    restrict access if not authorized

    :param f:
    :return: user_id
    """
    @wraps(f)
    def decorated_auth(*args, **kwargs):
        if 'Authorization' in request.headers:
            auth_header = request.headers.get('Authorization')
            access_token = auth_header.split(" ")[1]
            user_id = decode_token(access_token)
            if isinstance(user_id, int):
                user = User().find_by_id(user_id)
                if user:
                    g.user = {'user_id': user_id}
                    return f(*args, **kwargs)
                else:
                    return Response(
                        mimetype="application/json",
                        response=json.dumps({'status': 401,
                                             'error': 'user does not exist,'
                                                      ' invalid token'}),
                        status=401
                    )
            return Response(
                mimetype="application/json",
                response=json.dumps({'status': 400,
                                     'error': user_id}),
                status=400
            )
        else:
            return Response(
                mimetype="application/json",
                response=json.dumps({'status': 400,
                                     'error': 'Authentication token is'
                                              ' not available, please login'
                                              ' to get one'}),
                status=400
            )
    return decorated_auth


def admin_access(f):
    """
    restrict access if not Admin authorized

    :param f:
    :return: user_id
    """
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        user = User().find_by_id(g.user.get("user_id"))
        if not user.is_admin:
            return {'status': 401,
                    'message': 'Unauthorized access, you must be an admin to'
                               ' update incident records.'}, 401
        return f(*args, **kwargs)
    return wrapper_function
