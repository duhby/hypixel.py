"""A simple example that shows how to build achievement data."""

# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('gamerboy80')
            for achievement in player.achievements:
                achievement = hypixel.Achievement.from_type(achievement)
                if achievement:
                    print(achievement.name)
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
