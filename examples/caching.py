"""A simple example that shows how to use the cache."""

# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

import time

async def main():
    client = hypixel.Client('api-key', cache=True, cache_time=5)
    async with client:
        try:
            player = await client.player('gamerboy80')
            # Doesn't make any requests
            # Returns much faster than the first
            player = await client.player('gamerboy80')
            print(client.hypixel_cache_info)
            print(client.mojang_cache_info)
            time.sleep(5)
            # Makes new API requests
            player = await client.player('gamerboy80')
            client.clear_cache()
            # Makes new API requests
            player = await client.player('gamerboy80')
            client.clear_hypixel_cache()
            # Makes a new Hypixel API request
            # Doesn't make a new Mojang API request
            player = await client.player('gamerboy80')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
