# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

import time

description = """A simple example that shows how to use the cache."""

async def main():
    client = hypixel.Client('api-key', cache=True, cache_time=5)
    async with client:
        try:
            player = await client.player('duhby')
            # doesn't make any requests
            # returns much faster than the first
            player = await client.player('duhby')
            print(client.hypixel_cache_info)
            print(client.mojang_cache_info)
            time.sleep(5)
            # makes new api requests
            player = await client.player('duhby')
            client.clear_cache()
            # makes new api requests
            player = await client.player('duhby')
            client.clear_hypixel_cache()
            # makes a new hypixel api request
            # doesn't make a new mojang request
            player = await client.player('duhby')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
