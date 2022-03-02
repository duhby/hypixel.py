<div align="center">
<h1>hypixel.py (alpha)</h1>
<a href='https://discord.gg/PtsBc4b'>
    <img src='https://img.shields.io/discord/719949131497603123.svg?color=%237289da&label=discord&logo=discord&style=flat-square' alt='Discord Server'>
</a>
<a href='#'>
    <img src='https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fduhby%2Fhypixel.py&count_bg=%2344cc11&icon=&icon_color=%23555555&title=hits&edge_flat=true' alt='Hit Counter'>
</a>
<a href='https://docs.dubs.rip/en/latest/'>
    <img src='https://readthedocs.org/projects/hypixelpy/badge/?version=latest&style=flat-square' alt='Documentation Status'>
</a>
<a href='https://github.com/duhby/hypixel.py/blob/master/LICENSE'>
    <img src='https://img.shields.io/github/license/duhby/hypixel.py?style=flat-square&color=bright-green' alt='License'>
</a>
<h2>An asynchronous, feature-rich, Hypixel API wrapper for Python</h2>
</div>

## Why hypixel.py?
### Blazing fast.
Hypixel.py is fast and lightweight, using built in functions to achieve async timed lru caching, fast nested dataclass json sterilization, modern sane rate limit handling, and more.
### Fully asynchronous.
Hypixel.py is fully asynchronous and uses modern async/await python syntax. This means your program won't have to wait for your api requests to finish before running any more code.
### Minimal depdencies.
Hypixel.py uses built in libraries for everything possible so you don't need to worry about relying on more libraries than necessary.
### Marvelously clean syntax.
Hypixel.py uses dot syntax for all of its models so you can easily access any data point without worrying about dictionaries and strings.
### Highly maintained documentation.
Hypixel.py's documentation is highly maintained and provides a plentiful amount of examples to get you started.

## Getting Started
#### Check out the [documentation](#)!
#### Python 3.7 or higher is required.
To install hypixel.py simply install it from pypi under the name `hypixel.py` with pip or your favorite package manager.
```bash
    pip install hypixel.py
```
You can also add `[speed]` after hypixel.py to install [additional packages](#optional-packages) to enhance aiohttp performance automatically.
```bash
    pip install hypixel.py[speed]
```
### Optional Packages
- [aiodns](https://pypi.org/project/aiodns/), [brotlipy](https://pypi.org/project/brotlipy/), [cchardet](https://pypi.org/project/cchardet/) (to enhance aiohttp performance)

## Quick Example
```python
import hypixel
from hypixel import HypixelException
import aiohttp

async def main():
    client = hypixel.Client('api-key')
    async with client:
        try:
            player = await client.player('duhby')
            print(f'[{player.bedwars.level}✫] [{player.rank}] {player.name}')
        except HypixelException as error:
            print(error)

if __name__ == '__main__':
    asyncio.run(main())
```
More examples are available [here](https://github.com/duhby/hypixel.py/tree/master/examples).

## Links
- [Documentation](#)
- [Discord Server](#) <!-- https://discord.gg/PtsBc4b -->
