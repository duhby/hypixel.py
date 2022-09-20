hypixel.py (alpha)
==================

.. .. image:: https://img.shields.io/discord/719949131497603123.svg?color=%237289da&label=discord&logo=discord&style=for-the-badge
..    :target: https://discord.gg/PtsBc4b/
..    :alt: Discord
.. image:: https://img.shields.io/pypi/dm/hypixel.py?color=blueviolet&style=for-the-badge
   :target: https://pypi.python.org/pypi/hypixel.py/
   :alt: PyPI downloads
.. image:: https://img.shields.io/pypi/v/hypixel.py.svg?style=for-the-badge&logo=semantic-release&color=blue
   :target: https://pypi.python.org/pypi/hypixel.py/
   :alt: PyPI version info
.. image:: https://img.shields.io/github/license/duhby/hypixel.py?style=for-the-badge&color=bright-green
   :target: https://github.com/duhby/hypixel.py/blob/master/LICENSE/
   :alt: License


.. start_doc

Hypixel.py is a modern, asynchronous, feature-rich, Hypixel API wrapper for Python.

It aims to make the process of writing scripts that deal with the Hypixel API easier
to prevent frustration due to the complexity and inapplicability of the API in its current state.

* **Fast AF (for python)** --- Fast and lightweight by using built in libraries to achieve async timed lru caching, fast nested dataclass json sterilization, modern sane rate limit handling, etc.
* **More asynchronous than online learning** --- Has full asynchronicity and uses modern pythonic ``async`` and ``await`` syntax.
* **Cleaner than your room** --- Uses object oriented pythonic dot syntax for all of its models, so you can easily access any data point without worrying about dictionaries, strings, and any random inconsistencies you may encounter using the raw API.
* **S Tier Docs** --- Highly maintained documentation with an ample amount of examples to get you started. It also has the highest player model coverage and documentation.

.. end_doc


Getting Started
---------------

**Check out the** `examples <https://github.com/duhby/hypixel.py/tree/master/examples>`_ **and** `documentation <#>`_!

**Python 3.7+ is required (3.9 recommended)**

Installation
^^^^^^^^^^^^

To install hypixel.py, simply install it from pypi under the name ``hypixel.py`` with pip or your favorite package manager.

.. code:: sh

   pip install hypixel.py --upgrade

You can also append ``[speed]`` to install optional packages (see below) to enhance aiohttp and json performance automatically.
**Warning:** cchardet does not support python 3.10+ and subsequently will not be installed using [speed] if you're on 3.10 or higher.

.. code:: sh

   pip install hypixel.py[speed] --upgrade

Optional Packages
^^^^^^^^^^^^^^^^^

To ehnahce aiohttp performance:

- `aiodns <https://pypi.org/project/aiodns/>`_
- `brotlipy <https://pypi.org/project/brotlipy/>`_
- `cchardet <https://pypi.org/project/cchardet/>`_

To enhance json decoding (up to 4x faster):

- `ujson <https://pypi.org/project/ujson/>`_

Warning
^^^^^^^

If you are running python version 3.8 or higher on Windows, then you must add the following code before you start an event loop (asyncio.run):

.. code:: python

   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

Quick Example
^^^^^^^^^^^^^

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

**You can find more examples** `here <https://github.com/duhby/hypixel.py/tree/master/examples>`_

..
   Links
   -----

..
   `Documentation <#>`_
   `Discord Server <#>`_
