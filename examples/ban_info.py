"""A simple example that shows how to get watchdog and staff ban
info."""

# This example requires an api key

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            print(await client.bans())
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
