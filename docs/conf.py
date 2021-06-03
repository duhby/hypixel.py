# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "hypixel.py"
copyright = f"2021-{datetime.now().year}, duhby"

release = "0.0.1"


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
]

autodoc_member_order = 'bysource'

language = 'en'
exclude_patterns = ['_build']
pygments_style = 'friendly'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_favicon = './images/icon.png'
