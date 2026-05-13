from pydantic import BaseModel


class LoginRequest(BaseModel):

    username: str
    password: str


class Token(BaseModel):

    access_token: str
    token_type: str


class TokenData(BaseModel):

    username: str | None = None
