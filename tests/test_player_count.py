from aioresponses import aioresponses
import hypixel
import pytest


@pytest.mark.asyncio
async def test_player_count(generate_client, key):
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/playerCount?key={key}',
                payload={
                    "success":True,
                    "playerCount":100000,
                },
            )

            player_count = await client.player_count()
            assert player_count == 100000
