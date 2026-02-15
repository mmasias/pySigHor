from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Schema para login."""

    username: str
    password: str


class Token(BaseModel):
    """Schema para token JWT."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Schema para datos del token."""

    username: str | None = None
