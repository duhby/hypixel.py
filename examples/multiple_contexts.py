"""A simple example that shows how to use the same Client instance with multiple contexts."""

import hypixel
from hypixel import HypixelException
import asyncio

async def main():
    client = hypixel.Client()
    async with client:
        "Do stuff here"

    # Opening a new context will open a new aiohttp.ClientSession while keeping your
    # Client attributes
    async with client:
        "Do more stuff here"

if __name__ == '__main__':
    asyncio.run(main())
