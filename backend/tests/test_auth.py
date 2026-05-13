import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_login_exitoso(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "admin", "password": "admin"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_fallido(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "admin", "password": "wrong"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_endpoint_sin_token(client: AsyncClient):
    response = await client.get("/api/v1/aulas/")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_endpoint_con_token(client: AsyncClient, auth_token: str):
    response = await client.get(
        "/api/v1/aulas/",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
