import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_listar_aulas_vacias(client: AsyncClient, auth_token: str):
    response = await client.get(
        "/api/v1/aulas/",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_crear_aula(client: AsyncClient, auth_token: str):
    response = await client.post(
        "/api/v1/aulas/",
        json={"nombre": "A-101", "capacidad": 30},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "A-101"
    assert data["capacidad"] == 30


@pytest.mark.asyncio
async def test_crear_aula_duplicada(client: AsyncClient, auth_token: str):
    await client.post(
        "/api/v1/aulas/",
        json={"nombre": "B-201", "capacidad": 25},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    response = await client.post(
        "/api/v1/aulas/",
        json={"nombre": "B-201", "capacidad": 25},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_obtener_aula(client: AsyncClient, auth_token: str):
    crear = await client.post(
        "/api/v1/aulas/",
        json={"nombre": "C-301", "capacidad": 40},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    aula_id = crear.json()["id"]

    response = await client.get(
        f"/api/v1/aulas/{aula_id}",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json()["nombre"] == "C-301"


@pytest.mark.asyncio
async def test_eliminar_aula(client: AsyncClient, auth_token: str):
    crear = await client.post(
        "/api/v1/aulas/",
        json={"nombre": "D-401", "capacidad": 20},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    aula_id = crear.json()["id"]

    response = await client.delete(
        f"/api/v1/aulas/{aula_id}",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 204
