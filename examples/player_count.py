"""A simple example that shows how to get the current number of players."""

# This exmaple requies an api key

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            print(client.player_count())
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
