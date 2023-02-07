from aioresponses import aioresponses
from datetime import datetime, timezone
import pytest

from hypixel import Color
from hypixel import Game


def _test_guild(guild, id_):
    assert guild.id == id_
    assert guild.name == 'jakeygoat'
    assert guild.exp == 306224961
    assert guild.created == datetime(
        2017, 9, 20, 23, 15, 16, 134000,
        tzinfo=timezone.utc,
    )
    assert guild.level == 109.41
    assert guild.legacy_rank == 440

    rank0 = guild.ranks[0]
    rank1 = guild.ranks[1]
    rank2 = guild.ranks[2]
    rank3 = guild.ranks[3]
    assert rank0.name == 'OFFICER'
    assert rank0.default == False
    assert rank0.created == datetime(
        2018, 10, 2, 2, 15, 9, 56000,
        tzinfo=timezone.utc,
    )
    assert rank0.priority == 4
    assert rank0.tag == None

    assert rank1.name == 'Member'
    assert rank1.default == False
    assert rank1.created == datetime(
        2018, 10, 2, 2, 15, 9, 407000,
        tzinfo=timezone.utc,
    )
    assert rank1.priority == 3
    assert rank1.tag == None

    assert rank2.name == 'altsXD'
    assert rank2.default == False
    assert rank2.created == datetime(
        2018, 10, 2, 2, 15, 9, 804000,
        tzinfo=timezone.utc,
    )
    assert rank2.priority == 1
    assert rank2.tag == None

    assert rank3.name == 'Co Owner'
    assert rank3.default == False
    assert rank3.created == datetime(
        2018, 12, 23, 18, 55, 14, 276000,
        tzinfo=timezone.utc,
    )
    assert rank3.priority == 4
    assert rank3.tag == None

    assert rank0 > rank1
    assert rank2 < rank0

    assert guild.winners == 2409
    assert guild.experience_kings == 485494
    assert guild.most_online_players == 23
    assert guild.joinable == False
    assert guild.tag == 'NOLIFE'
    assert guild.tag_color == Color.from_type('DARK_GREEN')
    assert guild.description == 'big chungus'
    assert guild.preferred_games == [
        Game.from_type('BEDWARS'),
        Game.from_type('ARCADE'),
    ]
    assert guild.publicly_listed == False

    assert guild.game_exp[0] == (
        Game.from_type('GINGERBREAD'),
        429213,
    )
    assert guild.game_exp[-1] == (
        Game.from_type('SKYWARS'),
        26774440,
    )

    member0 = guild.members[0]
    member1 = guild.members[1]
    member2 = guild.members[2]
    assert member0.uuid == '24c182c6716b47c68f60a1be9045c449'
    assert member0.rank.name == 'Guild Master'
    assert member0.joined == datetime(
        2018, 8, 28, 2, 0, 19, 161000,
        tzinfo=timezone.utc,
    )
    assert member0.exp_history[
        datetime(
            2022, 10, 15, 0, 0,
            tzinfo=timezone.utc,
        )
    ] == 0
    assert member0.exp_history[
        datetime(
            2022, 10, 14, 0, 0,
            tzinfo=timezone.utc,
        )
    ] == 13047
    assert member0.quest_participation == 4396
    assert member0.name == None

    assert member1.uuid == '369d8ab8cded461091d1189acd3b44d2'
    assert member1.rank == rank1
    assert member1.joined == datetime(
        2018, 9, 11, 2, 19, 24, 312000,
        tzinfo=timezone.utc
    )
    assert member1.exp_history[
        datetime(
            2022, 10, 15, 0, 0,
            tzinfo=timezone.utc,
        )
    ] == 0
    assert member1.quest_participation == 43
    assert member1.name == None

    assert member2.uuid == 'cc7fbd331def4e67a02254df4ef05a4f'
    assert member2.rank == rank0
    assert member2.joined == datetime(
        2019, 2, 11, 4, 18, 40, 233000,
        tzinfo=timezone.utc
    )
    assert member2.exp_history[
        datetime(
            2022, 10, 15, 0, 0,
            tzinfo=timezone.utc,
        )
    ] == 0
    assert member2.quest_participation == 782
    assert member2.name == None


@pytest.mark.asyncio
async def test_guild(generate_client, key, utils):
    id_ = '59c2f6840cf25823b02a7141'
    player = '24c182c6716b47c68f60a1be9045c449'
    name = 'jakeygoat'
    payload = utils.response('guild')
    async for client in generate_client:
        with aioresponses() as m:
            m.get(
                f'https://api.hypixel.net/guild?key={key}&id={id_}',
                payload=payload
            )
            m.get(
                f'https://api.hypixel.net/guild?key={key}&player={player}',
                payload=payload
            )
            m.get(
                f'https://api.hypixel.net/guild?key={key}&name={name}',
                payload=payload
            )

            guild = await client.guild_from_id(id_)
            _test_guild(guild, id_)
            guild = await client.guild_from_player(player)
            _test_guild(guild, id_)
            guild = await client.guild_from_name(name)
            _test_guild(guild, id_)
