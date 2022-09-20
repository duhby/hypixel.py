.. currentmodule:: hypixel

API Reference
=============

This section outlines the API of hypixel.py.

Version Info
------------

There are two ways to query version information about the library.

.. data:: __version__

    A string representation of the version. E.g. ``'1.0.0rc1'``. Based off of :pep:`440`.

.. data:: version_info

    A named tuple that is similar to :obj:`py:sys.version_info`.

    Just like :obj:`py:sys.version_info` the valid values for ``releaselevel`` are
    'alpha', 'beta', 'candidate' and 'final'.

Client
------

.. attributetable:: Client

.. autoclass:: Client
    :members:
    :undoc-members:

Models
------

Models are dataclasses that are not meant to be manually constructed.

.. danger::

    These are **not intended to be created by users** and are **read-only**.

.. note::

    Although attributes are technically modifiable, it is not recommended
    to do so.

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

Games
~~~~~

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

.. attributetable:: Player

.. autoclass:: Player()
    :members:

PlayerData
~~~~~~~~~~

.. currentmodule:: hypixel.models.playerdata

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
    :undoc-members:

.. currentmodule:: hypixel

Types
~~~~~

.. attributetable:: ColorType

.. autoclass:: ColorType()
    :members:
    :undoc-members:

.. attributetable:: GameType

.. autoclass:: GameType()
    :members:
    :undoc-members:

Constants
---------

Constant values for doing stuff.

.. autoclass:: GameTypes

.. autoclass:: RankTypes

Utils
-----

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
