import asyncio
import datetime

from aioresponses import aioresponses
import hypixel
import pytest


@pytest.mark.asyncio
async def test_player(generate_client, key, utils):
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
                f'https://api.hypixel.net/player?key={key}&uuid={uuid}',
                payload=utils.response('player'),
            )

            player = await client.player(name)

            # These would be too much work to test, and are already
            # sufficiently tested in model tests.
            # assert player._data == utils.response('player')['player']
            # assert player.raw == utils.response('player')

            assert player.id == '5928e7937c007e009af27837'
            assert player.uuid == 'b423f64699f94694ad2366aa9647c606'
            assert player.first_login == datetime.datetime(2017, 5, 27, 2, 42, 27, 723000, tzinfo=datetime.timezone.utc)
            assert player.name == 'duhby'
            assert player.last_login == datetime.datetime(2023, 2, 8, 4, 53, 53, 920000, tzinfo=datetime.timezone.utc)
            assert player.last_logout == datetime.datetime(2023, 2, 8, 5, 10, 20, 282000, tzinfo=datetime.timezone.utc)
            assert player.achievements == utils.response('player')['player']['achievementsOneTime']
            player.build_achievements()
            assert player.achievements[0] == hypixel.Achievement.from_type('general_first_join')
            assert player.achievements[-1] == hypixel.Achievement.from_type('christmas2017_hunt_begins_2022')
            assert player.network_exp == 37412956
            assert player.karma == 10376990
            assert player.achievement_points == 4460
            assert player.current_gadget == 'GRAPPLING_HOOK'
            assert player.channel == 'PARTY'
            assert player.rank == 'MVP+'
            assert player.plus_color == hypixel.Color.from_type('DARK_RED')
            assert player.level == 170.54
            assert player.most_recent_game == hypixel.Game.from_id(58)

            # Arcade
            arcade = player.arcade
            assert arcade.coins == 3964483
            ctw = arcade.ctw
            assert ctw.captures == 5
            assert ctw.kills_assists == 281
            hypixel_says = arcade.hypixel_says
            assert hypixel_says.rounds == 840
            assert hypixel_says.wins == 12
            assert hypixel_says.top_score == 16
            assert hypixel_says.losses == 828
            assert hypixel_says.wlr == 0.01
            mini_walls = arcade.mini_walls
            assert mini_walls.kills == 388
            assert mini_walls.deaths == 475
            assert mini_walls.wins == 37
            assert mini_walls.final_kills == 128
            assert mini_walls.wither_kills == 38
            assert mini_walls.wither_damage == 2756
            assert mini_walls.arrows_hit == 109
            assert mini_walls.arrows_shot == 471
            assert mini_walls.kdr == 0.82
            party_games = arcade.party_games
            assert party_games.wins == 14
            assert party_games.wins_2 == 4
            assert party_games.wins_3 == 10
            assert party_games.total_wins == 28

            # Bedwars
            bedwars = player.bedwars
            assert bedwars.level == 367
            assert bedwars.coins == 1146395
            assert bedwars.kills == 13098
            assert bedwars.deaths == 21200
            assert bedwars.fall_deaths == 473
            assert bedwars.void_deaths == 11894
            assert bedwars.wins == 2219
            assert bedwars.losses == 2939
            assert bedwars.games == 5297
            assert bedwars.final_kills == 7051
            assert bedwars.final_deaths == 2948
            assert bedwars.fall_final_deaths == 71
            assert bedwars.void_final_deaths == 1285
            assert bedwars.beds_broken == 4275
            assert bedwars.beds_lost == 3202
            assert bedwars.winstreak == 42
            assert bedwars.exp == 1784766
            assert bedwars.kdr == 0.62
            assert bedwars.wlr == 0.76
            assert bedwars.fkdr == 2.39
            assert bedwars.bblr == 1.34
            solo = bedwars.solo
            assert solo.kills == 1814
            assert solo.deaths == 3743
            assert solo.fall_deaths == 55
            assert solo.void_deaths == 2344
            assert solo.wins == 175
            assert solo.losses == 855
            assert solo.games == 1062
            assert solo.final_kills == 1043
            assert solo.final_deaths == 781
            assert solo.fall_final_deaths == 7
            assert solo.void_final_deaths == 284
            assert solo.beds_broken == 1304
            assert solo.beds_lost == 844
            assert solo.kdr == 0.48
            assert solo.wlr == 0.2
            assert solo.fkdr == 1.34
            assert solo.bblr == 1.55
            doubles = bedwars.doubles
            assert doubles.kills == 5961
            assert doubles.deaths == 8820
            assert doubles.fall_deaths == 148
            assert doubles.void_deaths == 5044
            assert doubles.wins == 682
            assert doubles.losses == 1327
            assert doubles.games == 2085
            assert doubles.final_kills == 3271
            assert doubles.final_deaths == 1359
            assert doubles.fall_final_deaths == 27
            assert doubles.void_final_deaths == 662
            assert doubles.beds_broken == 2014
            assert doubles.beds_lost == 1463
            assert doubles.kdr == 0.68
            assert doubles.wlr == 0.51
            assert doubles.fkdr == 2.41
            assert doubles.bblr == 1.38
            threes = bedwars.threes
            assert threes.kills == 1696
            assert threes.deaths == 2743
            assert threes.fall_deaths == 72
            assert threes.void_deaths == 1463
            assert threes.wins == 350
            assert threes.losses == 300
            assert threes.games == 662
            assert threes.final_kills == 754
            assert threes.final_deaths == 314
            assert threes.fall_final_deaths == 8
            assert threes.void_final_deaths == 132
            assert threes.beds_broken == 337
            assert threes.beds_lost == 339
            assert threes.kdr == 0.62
            assert threes.wlr == 1.17
            assert threes.fkdr == 2.4
            assert threes.bblr == 0.99
            fours = bedwars.fours
            assert fours.kills == 3431
            assert fours.deaths == 5578
            assert fours.fall_deaths == 184
            assert fours.void_deaths == 2899
            assert fours.wins == 850
            assert fours.losses == 453
            assert fours.games == 1322
            assert fours.final_kills == 1840
            assert fours.final_deaths == 488
            assert fours.fall_final_deaths == 27
            assert fours.void_final_deaths == 205
            assert fours.beds_broken == 579
            assert fours.beds_lost == 547
            assert fours.kdr == 0.62
            assert fours.wlr == 1.88
            assert fours.fkdr == 3.77
            assert fours.bblr == 1.06
            teams = bedwars.teams
            assert teams.kills == 196
            assert teams.deaths == 316
            assert teams.fall_deaths == 14
            assert teams.void_deaths == 144
            assert teams.wins == 162
            assert teams.losses == 4
            assert teams.games == 166
            assert teams.final_kills == 143
            assert teams.final_deaths == 6
            assert teams.fall_final_deaths == 2
            assert teams.void_final_deaths == 2
            assert teams.beds_broken == 41
            assert teams.beds_lost == 9
            assert teams.kdr == 0.62
            assert teams.wlr == 40.5
            assert teams.fkdr == 23.83
            assert teams.bblr == 4.56

            # Blitz Survival Games
            blitz = player.blitz
            assert blitz.coins == 1030422
            assert blitz.kills == 36299
            assert blitz.deaths == 3898
            assert blitz.wins == 3893
            assert blitz.wins_solo == 3865
            assert blitz.wins_team == 0
            assert blitz.arrows_hit == 16
            assert blitz.arrows_shot == 51
            assert blitz.chests_opened == 35
            assert blitz.games == 7
            assert blitz.kdr == 9.31
            assert blitz.wlr == 1.0
            assert blitz.ar == 0.46

            # Duels
            duels = player.duels
            assert duels.coins == 915656
            assert duels.kills == 5982
            assert duels.deaths == 1995
            assert duels.wins == 6820
            assert duels.losses == 1974
            assert duels.melee_hits == 125397
            assert duels.melee_swings == 299949
            assert duels.arrows_hit == 1481
            assert duels.arrows_shot == 4523
            assert duels.wlr == 3.45
            assert duels.mr == 0.72
            assert duels.ar == 0.49
            assert duels.title == 'Legend III'
            blitz = duels.blitz
            assert blitz.kills == 0
            assert blitz.deaths == 1
            assert blitz.wins == 0
            assert blitz.losses == 1
            assert blitz.melee_hits == 23
            assert blitz.melee_swings == 96
            assert blitz.arrows_hit == 0
            assert blitz.arrows_shot == 0
            assert blitz.wlr == 0.0
            assert blitz.mr == 0.32
            assert blitz.ar == 0.0
            assert blitz.title == 'Rookie I'
            bow = duels.bow
            assert bow.kills == 1
            assert bow.deaths == 3
            assert bow.wins == 1
            assert bow.losses == 3
            assert bow.melee_hits == 0
            assert bow.melee_swings == 0
            assert bow.arrows_hit == 69
            assert bow.arrows_shot == 411
            assert bow.wlr == 0.33
            assert bow.mr == 0.0
            assert bow.ar == 0.2
            assert bow.title == 'Rookie I'
            boxing = duels.boxing
            assert boxing.kills == 0
            assert boxing.deaths == 0
            assert boxing.wins == 9
            assert boxing.losses == 4
            assert boxing.melee_hits == 1570
            assert boxing.melee_swings == 3151
            assert boxing.arrows_hit == 0
            assert boxing.arrows_shot == 0
            assert boxing.wlr == 2.25
            assert boxing.mr == 0.99
            assert boxing.ar == 0.0
            assert boxing.title == 'Rookie I'
            bridge = duels.bridge
            assert bridge.kills == 35
            assert bridge.deaths == 71
            assert bridge.wins == 87
            assert bridge.losses == 29
            assert bridge.melee_hits == 6869
            assert bridge.melee_swings == 21258
            assert bridge.arrows_hit == 518
            assert bridge.arrows_shot == 977
            assert bridge.wlr == 3.0
            assert bridge.mr == 0.48
            assert bridge.ar == 1.13
            assert bridge.title == 'Iron III'
            classic = duels.classic
            assert classic.kills == 282
            assert classic.deaths == 110
            assert classic.wins == 280
            assert classic.losses == 110
            assert classic.melee_hits == 5817
            assert classic.melee_swings == 16033
            assert classic.arrows_hit == 244
            assert classic.arrows_shot == 707
            assert classic.wlr == 2.55
            assert classic.mr == 0.57
            assert classic.ar == 0.53
            assert classic.title == 'Gold I'
            combo = duels.combo
            assert combo.kills == 0
            assert combo.deaths == 0
            assert combo.wins == 0
            assert combo.losses == 0
            assert combo.melee_hits == 4202
            assert combo.melee_swings == 11313
            assert combo.arrows_hit == 0
            assert combo.arrows_shot == 0
            assert combo.wlr == 0.0
            assert combo.mr == 0.59
            assert combo.ar == 0.0
            assert combo.title == 'Rookie I'
            mega_walls = duels.mega_walls
            assert mega_walls.kills == 0
            assert mega_walls.deaths == 0
            assert mega_walls.wins == 0
            assert mega_walls.losses == 0
            assert mega_walls.melee_hits == 0
            assert mega_walls.melee_swings == 0
            assert mega_walls.arrows_hit == 0
            assert mega_walls.arrows_shot == 0
            assert mega_walls.wlr == 0.0
            assert mega_walls.mr == 0.0
            assert mega_walls.ar == 0.0
            assert mega_walls.title == 'Rookie I'
            no_debuff = duels.no_debuff
            assert no_debuff.kills == 0
            assert no_debuff.deaths == 0
            assert no_debuff.wins == 0
            assert no_debuff.losses == 0
            assert no_debuff.melee_hits == 0
            assert no_debuff.melee_swings == 0
            assert no_debuff.arrows_hit == 0
            assert no_debuff.arrows_shot == 0
            assert no_debuff.wlr == 0.0
            assert no_debuff.mr == 0.0
            assert no_debuff.ar == 0.0
            assert no_debuff.title == 'Rookie I'
            op = duels.op
            assert op.kills == 0
            assert op.deaths == 1
            assert op.wins == 0
            assert op.losses == 1
            assert op.melee_hits == 110
            assert op.melee_swings == 437
            assert op.arrows_hit == 2
            assert op.arrows_shot == 12
            assert op.wlr == 0.0
            assert op.mr == 0.34
            assert op.ar == 0.2
            assert op.title == 'Rookie I'
            parkour = duels.parkour
            assert parkour.kills == 0
            assert parkour.deaths == 0
            assert parkour.wins == 0
            assert parkour.losses == 0
            assert parkour.melee_hits == 0
            assert parkour.melee_swings == 0
            assert parkour.arrows_hit == 0
            assert parkour.arrows_shot == 0
            assert parkour.wlr == 0.0
            assert parkour.mr == 0.0
            assert parkour.ar == 0.0
            assert parkour.title == 'Rookie I'
            skywars = duels.skywars
            assert skywars.kills == 0
            assert skywars.deaths == 0
            assert skywars.wins == 0
            assert skywars.losses == 0
            assert skywars.melee_hits == 0
            assert skywars.melee_swings == 0
            assert skywars.arrows_hit == 0
            assert skywars.arrows_shot == 0
            assert skywars.wlr == 0.0
            assert skywars.mr == 0.0
            assert skywars.ar == 0.0
            assert skywars.title == 'Rookie I'
            sumo = duels.sumo
            assert sumo.kills == 5642
            assert sumo.deaths == 1621
            assert sumo.wins == 6298
            assert sumo.losses == 1709
            assert sumo.melee_hits == 91570
            assert sumo.melee_swings == 195444
            assert sumo.arrows_hit == 0
            assert sumo.arrows_shot == 0
            assert sumo.wlr == 3.69
            assert sumo.mr == 0.88
            assert sumo.ar == 0.0
            assert sumo.title == 'Grandmaster II'
            # Does this even exist?
            tnt_games = duels.tnt_games
            assert tnt_games.kills == 0
            assert tnt_games.deaths == 0
            assert tnt_games.wins == 0
            assert tnt_games.losses == 0
            assert tnt_games.melee_hits == 0
            assert tnt_games.melee_swings == 0
            assert tnt_games.arrows_hit == 0
            assert tnt_games.arrows_shot == 0
            assert tnt_games.wlr == 0.0
            assert tnt_games.mr == 0.0
            assert tnt_games.ar == 0.0
            assert tnt_games.title == 'Rookie I'
            uhc = duels.uhc
            assert uhc.kills == 36
            assert uhc.deaths == 66
            assert uhc.wins == 36
            assert uhc.losses == 66
            assert uhc.melee_hits == 6937
            assert uhc.melee_swings == 24906
            assert uhc.arrows_hit == 548
            assert uhc.arrows_shot == 1941
            assert uhc.wlr == 0.55
            assert uhc.mr == 0.39
            assert uhc.ar == 0.39
            assert uhc.title == 'Rookie I'

            # Murder Mystery
            mm = player.murder_mystery
