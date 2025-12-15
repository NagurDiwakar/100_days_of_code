"""
Test joke endpoints
"""
import pytest
from httpx import AsyncClient
from unittest.mock import patch, AsyncMock


@pytest.mark.asyncio
async def test_get_random_joke(client: AsyncClient):
    """Test getting a random joke"""
    # Mock the external API
    mock_joke = {
        "setup": "Why did the chicken cross the road?",
        "punchline": "To get to the other side!",
        "type": "general"
    }
    
    with patch("app.services.joke_service.httpx.AsyncClient") as mock_client:
        mock_response = AsyncMock()
        mock_response.json.return_value = mock_joke
        mock_response.raise_for_status = AsyncMock()
        mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
        
        response = await client.get("/jokes/random")
        assert response.status_code == 200
        data = response.json()
        assert "setup" in data
        assert "punchline" in data


@pytest.mark.asyncio
async def test_list_jokes(client: AsyncClient):
    """Test listing jokes"""
    response = await client.get("/jokes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_joke_by_id_not_found(client: AsyncClient):
    """Test getting non-existent joke"""
    response = await client.get("/jokes/99999")
    assert response.status_code == 404
