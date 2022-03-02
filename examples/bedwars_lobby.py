import hypixel
from hypixel import HypixelException
import aiohttp

description = """A simple example showcasing hypixel.py's different features."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('duhby')
            print(f'[✫{player.bedwars.level}] [{player.rank}] {player.name}')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
