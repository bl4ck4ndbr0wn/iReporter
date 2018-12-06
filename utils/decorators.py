from functools import wraps
import json
from flask import request, Response, g

from app.api.v2.models.user import User


def jwt_required(f):
    """
    restrict access if not authorized

    :param f:
    :return: user_id
    """
    @wraps(f)
    def decorated_auth(*args, **kwargs):
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
                        g.user = {'user_id': user_id}
                        return f(*args, **kwargs)
                    return Response(
                                      mimetype="application/json",
                                      response=json.dumps({'error': 'user does not exist, invalid token'}),
                                      status=401
                                    )
                return Response(
                                  mimetype="application/json",
                                  response=json.dumps(user_id),
                                  status=400
                                )
        else:
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': 'Authentication token is not available, please login to get one'}),
                status=400
            )
    return decorated_auth
