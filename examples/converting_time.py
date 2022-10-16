"""A simple example that shows how to convert the default time to other
timezones."""

# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

try:
    # Python 3.9+
    from zoneinfo import ZoneInfo
except ImportError:
    # Python 3.7-8 (pip install backports.zoneinfo[tzdata])
    # This module also works for python 3.6, however hypixel.py does not
    from backports.zoneinfo import ZoneInfo

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('gamerboy80')
            # Can be None if in game privacy settings are changed
            if player.last_login:
                # List possible timezones with
                # zoneinfo.available_timezones()
                new_york = ZoneInfo('America/New_York')
                # Convert UTC time to America/New_York time
                # (accounts for daylight savings)
                print(player.last_login.astimezone(new_york))
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
