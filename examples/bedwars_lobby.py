"""A simple example showing how to display a full bedwars lobby
username."""

# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('gamerboy80')
            # Will display [None] as the rank if the player has no rank
            print(f'[{player.bedwars.level}✫] [{player.rank}] {player.name}')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
