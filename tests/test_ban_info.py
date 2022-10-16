from aioresponses import aioresponses
import pytest


@pytest.mark.asyncio
async def test_player_count(generate_client, key):
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/watchdogstats?key={key}',
                payload={
                    "success": True,
                    "watchdog_lastMinute": 0,
                    "staff_rollingDaily": 1084,
                    "watchdog_total": 8167376,
                    "watchdog_rollingDaily": 1555,
                    "staff_total": 3355129,
                },
            )

            bans = await client.bans()
            assert bans.staff_day == 1084
            assert bans.staff_total == 3355129
            assert bans.watchdog_day == 1555
            assert bans.watchdog_recent == 0
            assert bans.watchdog_total == 8167376
