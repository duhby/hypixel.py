from setuptools import setup
import re

with open('hypixel/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

extras_require = {
    "speed": [
        "aiodns>=1.1",
        "Brotlipy",
        "cchardet",
    ]
}

packages = [
    'hypixel',
    'hypixel.constants',
    'hypixel.models',
    'hypixel.models.playerdata',
]

classifiers = [
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',
    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.7',
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
    long_description_content_type="text/markdown",
    url='https://github.com/duhby/hypixel.py',
    classifiers=classifiers,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.7',
)
