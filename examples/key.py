# This example requires an api key (obviously)

import hypixel
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example that shows how to get a key's queries."""

async def main():
    client = hypixel.Client()
    async with client:
        try:
            print(await client.key('api-key'))
            # If you passed a key into the client,
            # you can get its info as follows
            print(await client.key(client.keys[0]))
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
