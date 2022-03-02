import hypixel
from hypixel.errors import HypixelException
import asyncio

description = """A simple example that shows how to use the same Client instance with multiple contexts."""

async def main():
    client = hypixel.Client()
    async with client:
        "Do stuff here"

    # Opening a new context will open a new aiohttp.ClientSession but keep your hypixel.Client attributes
    async with client:
        "Do more stuff here"

if __name__ == '__main__':
    asyncio.run(main())
