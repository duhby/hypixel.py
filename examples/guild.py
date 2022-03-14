# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example that shows how to get a guild's info."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            guild = await client.guild_by_player('gamerboy80')
            # guild = await client.guild_by_name('jakeygoat')
            print(guild.name)
            print(guild.tag)
            print(guild.level)
            print(guild.description)
            print(guild.created.strftime('%A, %b %d %Y'))
            for rank in guild.ranks:
                print(rank.name)
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
