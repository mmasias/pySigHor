from app.schemas.aula import AulaCreate, AulaUpdate, AulaResponse
from app.schemas.edificio import EdificioCreate, EdificioUpdate, EdificioResponse
from app.schemas.programa import ProgramaCreate, ProgramaUpdate, ProgramaResponse
from app.schemas.curso import CursoCreate, CursoUpdate, CursoResponse
from app.schemas.profesor import ProfesorCreate, ProfesorUpdate, ProfesorResponse
from app.schemas.recurso import RecursoCreate, RecursoUpdate, RecursoResponse
from app.schemas.auth import LoginRequest, Token, TokenData

__all__ = [
    "AulaCreate", "AulaUpdate", "AulaResponse",
    "EdificioCreate", "EdificioUpdate", "EdificioResponse",
    "ProgramaCreate", "ProgramaUpdate", "ProgramaResponse",
    "CursoCreate", "CursoUpdate", "CursoResponse",
    "ProfesorCreate", "ProfesorUpdate", "ProfesorResponse",
    "RecursoCreate", "RecursoUpdate", "RecursoResponse",
    "LoginRequest", "Token", "TokenData",
]
