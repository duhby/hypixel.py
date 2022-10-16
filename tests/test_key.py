from aioresponses import aioresponses
import pytest


@pytest.mark.asyncio
async def test_key(generate_client, key):
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

            key_ = await client.key(key)
            assert key_.key == key
            assert key_.owner == 'b423f646-99f9-4694-ad23-66aa9647c606'
            assert key_.limit == 120
            assert key_.queries == 2343300
            assert key_.recent_queries == 3
