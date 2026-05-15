from pydantic import BaseModel, ConfigDict


class PreferenciaResponse(BaseModel):
    recurso_id: int
    nombre_recurso: str
    prioridad: int
    model_config = ConfigDict(from_attributes=True)


class PreferenciaUpdate(BaseModel):
    recurso_ids: list[int]
