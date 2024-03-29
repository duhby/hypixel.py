"""A simple example that shows how to get a player's first login."""

# This exmaple requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('gamerboy80')
            print(player.first_login.strftime('%A, %b %d %Y'))
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
