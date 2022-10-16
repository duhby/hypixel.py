import asyncio

from aioresponses import aioresponses
import pytest


@pytest.mark.asyncio
async def test_player_friends(generate_client, key):
    name = 'duhby'
    uuid = 'b423f64699f94694ad2366aa9647c606'
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.mojang.com/users/profiles/minecraft/{name}',
                payload={
                    "name": name,
                    "id": uuid,
                },
            )
            m.get(
                f'https://api.hypixel.net/friends?key={key}&uuid={uuid}',
                payload={
                    "success": True,
                    "uuid": "b423f64699f94694ad2366aa9647c606",
                    "records": [
                        {   # second
                            "_id": "60a9b7e10cf2b2d054c428f2",
                            "uuidSender": "b423f64699f94694ad2366aa9647c606",
                            "uuidReceiver": "4ffa3b3abeb64fee89a0f7697c55c92c",
                            "started": 1621735393064
                        },
                        {   # fourth
                            "_id": "60d34da20cf2b2d054e8289a",
                            "uuidSender": "b423f64699f94694ad2366aa9647c606",
                            "uuidReceiver": "7289394c9ad843b48213c3e338e1490f",
                            "started": 1624460706957,
                        },
                        {   # first
                            "_id": "609ff0eb0cf2b2d054b99ec8",
                            "uuidSender": "b423f64699f94694ad2366aa9647c606",
                            "uuidReceiver": "4536c13fb3a34eaa908fee05507d98a0",
                            "started": 1621094635296,
                        },
                        {   # third
                            "_id": "60d28c440cf2b2d054e782a0",
                            "uuidSender": "b423f64699f94694ad2366aa9647c606",
                            "uuidReceiver": "29cd08d9fdc84207a504feaca1da2aae",
                            "started": 1624411204553,
                        },
                    ],
                },
                repeat=True,
            )

            # Also tests utils.convert_id
            friends = await client.player_friends(name)
            assert len(friends) == 4
            for friend in friends:
                assert friend.uuid != uuid

            friends_sorted = await client.player_friends(uuid, sort=True)
            for friend in friends_sorted:
                assert friend in friends
            assert friends_sorted[-1].started > friends_sorted[0].started
