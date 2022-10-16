from setuptools import setup
import re


with open('hypixel/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(),
        re.MULTILINE
    ).group(1)

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

extras_require = {
    'speed': [
        'aiodns==3.0.0',
        'brotlipy==0.7.0',
        'cchardet==2.1.7; python_version < "3.10"',
        'ujson==5.5.0',
    ],
    'docs': [
        'sphinx==5.1.1',
        'sphinxcontrib_trio==1.1.2',
        'furo==2022.9.15',
        'sphinx_copybutton==0.5.0',
        'sphinx_design==0.3.0',
    ],
    'test': [
        'pytest==7.1.3',
        'pytest-asyncio==0.19.0',
        'pytest-cov==4.0.0',
        'aioresponses==0.7.3',
    ]
}

packages = [
    'hypixel',
    'hypixel.models',
    'hypixel.models.player',
]

classifiers = [
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',
    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='hypixel.py',
    author='duhby',
    license='MIT',
    version=version,
    packages=packages,
    description='A Python wrapper for the Hypixel API',
    long_description=readme,
    long_description_content_type="text/x-rst",
    url='https://github.com/duhby/hypixel.py',
    classifiers=classifiers,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.8',
)
