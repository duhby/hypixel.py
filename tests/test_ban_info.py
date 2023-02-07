from aioresponses import aioresponses
import pytest


@pytest.mark.asyncio
async def test_ban_info(generate_client, key, utils):
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/watchdogstats?key={key}',
                payload=utils.response('ban_info'),
            )

            bans = await client.bans()
            assert bans.staff_day == 1084
            assert bans.staff_total == 3355129
            assert bans.watchdog_day == 1555
            assert bans.watchdog_recent == 0
            assert bans.watchdog_total == 8167376
