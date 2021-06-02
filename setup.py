from setuptools import setup
import re

with open('hypixel/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

# extras_require = {
#     'docs': [
#         'sphinx==4.0.2',
#         'sphinxcontrib_trio==1.1.2',
#     ]
# }

classifiers = [
    # 'Development Status :: 5 - Production/Stable',
    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

packages = [
    'hypixel'
]

setup(
    name='hypixel.py',
    author='duhby',
    url='https://github.com/duhby/hypixel.py',
    project_urls={"Documentation": "https://docs.dubs.rip/en/latest"},
    version=version,
    packages=packages,
    license='MIT',
    description='A Python wrapper for the Hypixel API',
    long_description=readme,
    long_description_content_type="text/markdown",
    imstall_requires=requirements,
    # extras_require=extras_require,
    python_requires='>=3.6',
    classifiers=classifiers,
)
