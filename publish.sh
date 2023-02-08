#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e
# Import secrets
source secrets.sh

# Check if we're on a tagged commit
if [[ "$(git describe)" == *-* ]]; then
    echo "Error:" 1>&2
    echo "  Can't package a non-tagged commit." 1>&2
    echo "  Your current git commit isn't tagged with a proper version." 1>&2
    echo "  Try 'git tag -a' first" 1>&2
    exit 1
fi

# Install dependencies
python -m pip install -e .[test]
python -m pip install -e .[data]
# Run tests
PYTHONPATH=. pytest --cov=hypixel --cov-report term

# Remove old builds if they exist
rm -rfv dist build hypixel.py.egg-info
# Build package
python -m build
# Publish package
twine upload dist/* -u$PYPI_USERNAME -p$PYPI_TOKEN
