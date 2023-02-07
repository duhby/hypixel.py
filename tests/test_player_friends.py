# import asyncio

# from aioresponses import aioresponses
# import pytest


# @pytest.mark.asyncio
# async def test_player_friends(generate_client, key, utils):
#     name = 'duhby'
#     uuid = 'b423f64699f94694ad2366aa9647c606'
#     async for client in generate_client:
#         with aioresponses() as m:
#             m.get(
#                 f'https://api.mojang.com/users/profiles/minecraft/{name}',
#                 payload={
#                     "name": name,
#                     "id": uuid,
#                 },
#             )
#             m.get(
#                 f'https://api.hypixel.net/friends?key={key}&uuid={uuid}',
#                 payload=utils.response('player_friends'),
#                 repeat=True,
#             )

#             # Also tests utils.convert_id
#             friends = await client.player_friends(name)
#             assert len(friends) == 4
#             for friend in friends:
#                 assert friend.uuid != uuid

#             friends_sorted = await client.player_friends(uuid, sort=True)
#             for friend in friends_sorted:
#                 assert friend in friends
#             assert friends_sorted[-1].started > friends_sorted[0].started
