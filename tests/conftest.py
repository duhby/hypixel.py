import asyncio
import sys
import uuid

import hypixel
import pytest


@pytest.fixture
def key():
    return str(uuid.uuid4())


@pytest.fixture
async def generate_client(key):
    async with hypixel.Client(key) as client:
        yield client


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.new_event_loop()
    version = sys.version_info[:3]
    try:
        if (
            isinstance(
                asyncio.get_event_loop_policy(),
                asyncio.DefaultEventLoopPolicy,
            )
            and sys.platform.startswith('win')
            and (3, 8, 0) <= version < (3, 10, 8) # Fixed in 3.10.8
        ):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except AttributeError:
        pass
    yield loop
    loop.close()
