import datetime

import jwt
from django.conf import settings
import typing


def create_temp_token(attrs: typing.Union[dict, None] = None) -> str:
    payload = {
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(hours=settings.TEMP_TOKEN_LIFETIME),
    }
    if isinstance(attrs, dict):
        payload.update(attrs)
    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def decode_temp_token(temp_token: str) -> dict:
    decoded_data = jwt.decode(temp_token, settings.SECRET_KEY, algorithms=["HS256"])
    return decoded_data
