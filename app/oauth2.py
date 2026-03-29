import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime,timedelta,timezone
from . import schemas,database,models
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import Settings as settings
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "20ddcf7376d59e3c4958d4d3dbedf3a1e9dac5666cf2e48c33fc0bad08657636"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

        id: Optional[str] = payload.get("user_id")

        if id is None:
            raise credentials_exception
    
        token_data = schemas.tokenData(id=id)

    except InvalidTokenError:
        raise credentials_exception
    
    return token_data

    
def get_current_user(token:str = Depends(oauth2_scheme), db : Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials", 
                                          headers={"WWW-Authenticate":"Bearer"})
    
    return verify_token(token,credentials_exception)

 