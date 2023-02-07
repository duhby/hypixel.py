from aioresponses import aioresponses
import hypixel
import pytest


@pytest.mark.asyncio
async def test_player_count(generate_client, key, utils):
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/playerCount?key={key}',
                payload=utils.response('player_count'),
            )

            player_count = await client.player_count()
            assert player_count == 100000
