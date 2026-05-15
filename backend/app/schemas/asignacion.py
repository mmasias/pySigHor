from pydantic import BaseModel


class AsignacionUpdate(BaseModel):
    curso_ids: list[int]
