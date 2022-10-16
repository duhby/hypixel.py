"""Tests for general hypixel.Client methods."""

from aioresponses import aioresponses
import hypixel.errors
import pytest
import uuid


@pytest.mark.asyncio
async def test_add_and_remove_key(generate_client):
    async for client in generate_client:
        new_key = str(uuid.uuid4())

        client.add_key(new_key)
        assert new_key in client.keys

        client.remove_key(new_key)
        assert new_key not in client.keys


@pytest.mark.asyncio
async def test_get_name(generate_client):
    name = 'duhby'
    uuid = 'b423f64699f94694ad2366aa9647c606'
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.mojang.com/user/profile/{uuid}',
                payload={
                    "id": uuid,
                    "name": name,
                },
            )

            assert name == await client.get_name(uuid)


@pytest.mark.asyncio
async def test_get_uuid(generate_client):
    name = 'duhby'
    uuid = 'b423f64699f94694ad2366aa9647c606'
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.mojang.com/users/profiles/minecraft/{name}',
                payload={
                    "name": name,
                    "id": uuid,
                },
            )

            assert uuid == await client.get_uuid(name)


@pytest.mark.asyncio
async def test_validate_keys(generate_client, key):
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/key?key={key}',
                payload={
                    "success": True,
                    "record": {
                        "key": key,
                        "owner": "b423f646-99f9-4694-ad23-66aa9647c606",
                        "limit": 120,
                        "queriesInPastMin": 3,
                        "totalQueries": 2343300
                    },
                },
            )
            assert await client.validate_keys() == None

            with pytest.raises(hypixel.MalformedApiKey):
                client.add_key('asdf')
                await client.validate_keys()
            client.remove_key('asdf')

        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/key?key={key}',
                payload={
                    "success": False,
                    "cause": "Invalid API key",
                },
                status=403,
            )
            with pytest.raises(hypixel.InvalidApiKey):
                await client.validate_keys()
