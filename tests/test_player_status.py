import asyncio

from aioresponses import aioresponses
import hypixel
import pytest


@pytest.mark.asyncio
async def test_player_status_offline(generate_client, key, utils):
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
            m.get(
                f'https://api.hypixel.net/status?key={key}&uuid={uuid}',
                payload=utils.response('player_status_offline'),
            )

            status = await client.player_status(name)
            assert status.online == False
            assert status.game is None
            assert status.mode is None
            assert status.map is None


@pytest.mark.asyncio
async def test_player_status_online(generate_client, key, utils):
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
            m.get(
                f'https://api.hypixel.net/status?key={key}&uuid={uuid}',
                payload=utils.response('player_status_online'),
            )

            status = await client.player_status(name)
            assert status.online == True
            assert type(status.game) == hypixel.Game
            assert status.game.id == 58
            assert status.game.standard_name == 'Bed Wars'
            assert status.mode == 'BEDWARS_FOUR_FOUR'
            assert status.map == 'Invasion'
