# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

from uuid import UUID

__doc__ = """A simple example showing how to handle leaderboard models."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            leaderboards = await client.leaderboards()
            bedwars = leaderboards['BEDWARS']
            # Can also use bedwars[0] instead of next()
            level = next((
                lb for lb in bedwars if lb.title == 'Level'
            ), None)
            print(f'{level.prefix} {level.title}:')
            # Splices for top 10 instead of top 100
            for index, player in enumerate(level.leaders[:10]):
                # Requests from mojang's api
                print(f'#{index + 1} {await client.get_name(player)}')

            player = 'gamerboy80'
            uuid = await client.get_uuid(player)
            uuid = str(UUID(uuid))
            index = level.leaders.index(uuid)
            print(f'#{index + 1} {player}')

        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
