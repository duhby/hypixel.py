Hypixel.py Documentation
========================

.. include:: ../README.rst
    :start-after: .. start_doc
    :end-before: .. end_doc

What does it look like? Here's an example of a simple hypixel.py program:

.. code:: python

    import hypixel
    from hypixel import HypixelException
    import asyncio

    async def main():
        client = hypixel.Client('api-key')
        async with client:
            try:
                player = await client.player('gamerboy80')
                print(f'[{player.bedwars.level}✫] [{player.rank}] {player.name}')
            except HypixelException as error:
                print(error)

    if __name__ == '__main__':
        asyncio.run(main())

If you replace ``api-key`` with a valid api key, you'll get something like this as a result:

.. code::

    >>> [1607✫] [YOUTUBE] gamerboy80


.. .. tab-set

..     .. tab-item:: Label1

..         Content 1

..     .. tab-item:: Label2

..         Content 2


Getting Started
---------------

.. toctree::
    :maxdepth: 1

    quickstart
    intro
    examples

API Reference
-------------

.. toctree::
    :maxdepth: 1

    api
