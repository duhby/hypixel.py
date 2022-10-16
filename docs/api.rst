.. currentmodule:: hypixel

API Reference
=============

This section outlines the API of hypixel.py.

Version Info
------------

There are two ways to query version information about the library.

.. data:: __version__

    A string representation of the version. E.g. ``'1.0.0rc1'``. Based off of
    :pep:`440`.

.. data:: version_info

    A named tuple that is similar to :obj:`py:sys.version_info`.

    Just like :obj:`py:sys.version_info` the valid values for ``releaselevel``
    are 'alpha', 'beta', 'candidate' and 'final'.

Client
------

.. attributetable:: Client

.. autoclass:: Client
    :members:

API Models
----------

API Models are dataclasses that are not meant to be manually constructed.

.. danger::

    These are **not intended to be created by users** and should be treated as
    **read-only**.

.. note::

    Although attributes are technically modifiable, it is not recommended to do
    so.

Bans
~~~~

.. attributetable:: Bans

.. autoclass:: Bans()
    :members:
    :undoc-members:

Friend
~~~~~~

.. attributetable:: Friend

.. autoclass:: Friend()
    :members:
    :undoc-members:

.. Games
.. ~~~~~

.. .. attributetable:: Game

.. .. autoclass:: Game()
..     :members:
..     :undoc-members:

.. .. attributetable:: GameCount

.. .. autoclass:: GameCount()
..     :members:
..     :undoc-members:

.. .. attributetable:: GameCounts

.. .. autoclass:: GameCounts()
..     :members:
..     :undoc-members:

Guild
~~~~~

.. attributetable:: Guild

.. autoclass:: Guild()
    :members:
    :undoc-members:

.. attributetable:: GuildMember

.. autoclass:: GuildMember()
    :members:
    :undoc-members:

.. attributetable:: GuildRank

.. autoclass:: GuildRank()
    :members:
    :undoc-members:

Key
~~~

.. attributetable:: Key

.. autoclass:: Key()
    :members:
    :undoc-members:

Leaderboards
~~~~~~~~~~~~

.. attributetable:: Leaderboard

.. autoclass:: Leaderboard()
    :members:
    :undoc-members:

Player
~~~~~~

.. currentmodule:: hypixel.models.player

.. attributetable:: Player

.. autoclass:: Player()
    :members:

.. attributetable:: Arcade

.. autoclass:: Arcade()
    :members:
    :undoc-members:

.. attributetable:: CaptureTheWool

.. autoclass:: CaptureTheWool()
    :members:
    :undoc-members:

.. attributetable:: HypixelSays

.. autoclass:: HypixelSays()
    :members:
    :undoc-members:

.. attributetable:: MiniWalls

.. autoclass:: MiniWalls()
    :members:
    :undoc-members:

.. attributetable:: PartyGames

.. autoclass:: PartyGames()
    :members:
    :undoc-members:

.. attributetable:: Bedwars

.. autoclass:: Bedwars()
    :members:

.. attributetable:: BedwarsMode

.. autoclass:: BedwarsMode()
    :members:

.. attributetable:: Blitz

.. autoclass:: Blitz()
    :members:
    :undoc-members:

.. attributetable:: Duels

.. autoclass:: Duels()
    :members:
    :undoc-members:

.. attributetable:: DuelsMode

.. autoclass:: DuelsMode()
    :members:
    :undoc-members:

.. attributetable:: MurderMystery

.. autoclass:: MurderMystery()
    :members:
    :undoc-members:

.. attributetable:: MurderMysteryMode

.. autoclass:: MurderMysteryMode()
    :members:
    :undoc-members:

.. attributetable:: Paintball

.. autoclass:: Paintball()
    :members:
    :undoc-members:

.. attributetable:: Parkour

.. autoclass:: Parkour()
    :members:
    :undoc-members:

.. attributetable:: ParkourLobby

.. autoclass:: ParkourLobby()
    :members:
    :undoc-members:

.. attributetable:: Skywars

.. autoclass:: Skywars()
    :members:
    :undoc-members:

.. attributetable:: SkywarsMode

.. autoclass:: SkywarsMode()
    :members:
    :undoc-members:

.. attributetable:: Socials

.. autoclass:: Socials()
    :members:
    :undoc-members:

.. attributetable:: TurboKartRacers

.. autoclass:: TurboKartRacers()
    :members:
    :undoc-members:

.. attributetable:: TntGames

.. autoclass:: TntGames()
    :members:
    :undoc-members:

.. attributetable:: Uhc

.. autoclass:: Uhc()
    :members:
    :undoc-members:

.. attributetable:: UhcMode

.. autoclass:: UhcMode()
    :members:
    :undoc-members:

.. attributetable:: WoolGames

.. autoclass:: WoolGames()
    :members:
    :undoc-members:

.. attributetable:: WoolGamesMode

.. autoclass:: WoolGamesMode()
    :members:
    :undoc-members:

.. currentmodule:: hypixel

Status
~~~~~~

.. attributetable:: Status

.. autoclass:: Status()
    :members:
    :undoc-members:

Data Classes
------------

These classes are data containers.

They hold metadata for what would otherwise be arbitrary strings returned by the
API.

Color
~~~~~

.. attributetable:: Color

.. autoclass:: Color()
    :members:

Game
~~~~

.. attributetable:: Game

.. autoclass:: Game()
    :members:

Utilities
---------

.. attributetable:: ExponentialBackoff

.. autoclass:: ExponentialBackoff
    :members:
    :undoc-members:

Exceptions
----------

.. autoexception:: HypixelException

.. autoexception:: ArgumentError

.. autoexception:: InvalidPlayerId

.. autoexception:: PlayerNotFound

.. autoexception:: KeyNotFound

.. autoexception:: ApiError

.. autoexception:: TimeoutError

.. autoexception:: RateLimitError

.. autoexception:: InvalidApiKey

.. autoexception:: MalformedApiKey

.. autoexception:: KeyRequired

.. autoexception:: ClosedSession

.. autoexception:: LoopPolicyError

.. autoexception:: GuildNotFound


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`Exception`
        - :exc:`HypixelException`
            - :exc:`ApiError`
                - :exc:`RateLimitError`
                - :exc:`TimeoutError`
            - :exc:`ArgumentError`
                - :exc:`GuildNotFound`
                - :exc:`InvalidApiKey`
                    - :exc:`KeyRequired`
                    - :exc:`MalformedApiKey`
                - :exc:`InvalidPlayerId`
                - :exc:`KeyNotFound`
                - :exc:`PlayerNotFound`
            - :exc:`ClosedSession`
            - :exc:`LoopPolicyError`
