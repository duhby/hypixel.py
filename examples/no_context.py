import hypixel
from hypixel.errors import HypixelException
import asyncio

description = """A simple example that shows how to use hypixel.Client without a context manager."""

async def main():
    client = hypixel.Client()

    try:
        "Do stuff here"
    except HypixelException as error:
        print(error)

    # make sure this is awaited before the program ends
    await client.close()

if __name__ == '__main__':
    asyncio.run(main())
