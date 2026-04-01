from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "f58a1b7f2aaed90bb80d6d62ffb562f699d9ccfaf7242517bc7a188028d389f3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt