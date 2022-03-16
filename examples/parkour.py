# This example requires an api key

import hypixel
from hypixel import utils
from hypixel import HypixelException
import asyncio

__doc__ = """A simple example showing how to display a player's parkour times."""

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('gamerboy80')
            parkour = player.parkour
            print(
                "Arcade: "
                f"completed on {parkour.arcade.completed.strftime('%A, %b %d %Y')} "
                # datetime.timedelta does not have its own strftime function.
                f"in {utils.strfdelta(parkour.arcade.time)}"
            )

            # Loop through every ParkourLobby object
            for i, lobby in enumerate(parkour):
                if lobby:
                    mode = parkour._modes[i]
                    print(f"{mode:<15} {utils.strfdelta(lobby.time):<10} {lobby.completed.year}")
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
