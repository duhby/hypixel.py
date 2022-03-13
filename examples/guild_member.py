# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example showing how to get a guild's member."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            guild = await client.guild_by_player('gamerboy80')
            # guild = await client.guild_by_name('jakeygoat')
            uuid = await client.get_uuid('gamerboy80')
            member = next((
                member for member in guild.members if member.uuid == uuid
            ), None)
            print(member)
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
