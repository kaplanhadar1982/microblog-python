import jwt
from datetime import datetime,timedelta
from decouple import config

def encode_auth_token(id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=500),
            'iat': datetime.utcnow(),
            'sub': id
        }
        return jwt.encode(
            payload,
            config("SECRET_KEY", cast=str),
            algorithm='HS256'
        )
    except Exception as e:
        return e

    
def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token,config("SECRET_KEY", cast=str))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'