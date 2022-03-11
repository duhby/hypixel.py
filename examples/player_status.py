# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example that shows how to get a player's status."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            # Attributes can be False and None if in game privacy settings are changed
            print(await client.player_status('gamerboy80'))
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
