import jwt
import api.models
from datetime import datetime
from graphql_jwt.settings import jwt_settings
    
def jwt_payload(user, context=None):
    jwt_datetime = datetime.now() + jwt_settings.JWT_EXPIRATION_DELTA
    jwt_expires = int(jwt_datetime.timestamp())
    payload = {}
    payload['username'] = str(user.username) # For library compatibility
    payload['sub'] = str(user.id)
    payload['sub_name'] = user.username
    payload['sub_email'] = user.email
    payload['expire_time'] = jwt_expires
    return payload