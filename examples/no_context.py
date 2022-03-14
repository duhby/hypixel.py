import hypixel
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example that shows how to use hypixel.Client without a context manager."""

async def main():
    client = hypixel.Client()

    try:
        "Do stuff here"
    except HypixelException as error:
        print(error)

    # Make sure this is awaited before your script ends
    await client.close()

if __name__ == '__main__':
    asyncio.run(main())
