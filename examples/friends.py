"""
A simple example that shows how to get and use player_friends data.

.. note::
    Only shows friends the player is currently friends with.

.. warning::
    Methods referenced in this example have been removed.
"""

# This exmaple requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            # Sort sorts the friends list from earliest to latest
            friends = await client.player_friends('gamerboy80', sort=True)
            earliest = friends[0]
            name = await client.get_name(earliest.uuid)
            print(f'First friend: {name}')

            latest = friends[-1]
            name = await client.get_name(latest.uuid)
            print(f'Latest friend: {name}')

            amount = len(friends)
            print(f'Has {amount} friends')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
