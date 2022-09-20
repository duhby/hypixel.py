"""A simple example showing how to display a player's parkour times."""

# This example requires an api key

import hypixel
from hypixel import utils
from hypixel import HypixelException
import asyncio

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

            # To compare another player's times
            # Kinda messy, but it shows the functionality
            # len() and subscripting[int] also work on Parkour objects, however len() always returns
            # the total amount, even if attributes are None, so subscripting 2 objects with the same
            # index always returns the same attribute.
            player2 = await client.player('technoblade')
            parkour2 = player2.parkour
            for i, (p1, p2) in enumerate(zip(parkour, parkour2)):
                if p1 and p2:
                    if p1.time < p2.time:
                        print(f"{parkour._modes[i]}: {player.name} with {p1.time}")
                    else:
                        print(f"{parkour._modes[i]}: {player2.name} with {p2.time}")
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
