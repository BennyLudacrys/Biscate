from functools import wraps

import jwt
from flask import request
from jwt import ExpiredSignatureError, InvalidTokenError

from flaskauth.models.user import User
from flaskauth.service.tokenservice import jwtDecode
from flaskauth.service.api_response import success, error


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][7:]
        if not token:
            return error({}, 'Authorization token required', 401)
        try:
            data = jwt.decode(token, '7vgtdjh_fgWQgdhLbas9df9409sf6a6ds4f3435fa64ˆGggfXV6Miy', algorithms=['HS256'])
            user = User.query.filter_by(id=data['sub']).first()
            return f(user, *args, **kwargs)
        except ExpiredSignatureError:
            return error({}, 'Token has expired', 401)
        except InvalidTokenError:
            return error({}, 'Invalid token', 401)
        except Exception as e:
            return error({}, f'Error decoding token: {str(e)}', 401)

    return decorator


def auth_optional(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        user = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][7:]
            try:
                data = jwtDecode(token)
                user = User.query.filter_by(id=data['sub']).first()
            except:
                return error({}, 'Invalid token2', 401)
        return f(user, *args, **kwargs)

    return decorator
