# Heavily inspired by Rapptz' discord.py docs:
# https://github.com/Rapptz/discord.py/blob/master/docs/conf.py

# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "hypixel.py"
copyright = f"2021-{datetime.now().year}, dubs"

release = "0.0.1"


# -- General configuration ---------------------------------------------------

extensions = [
    'builder',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'details',
    'attributetable',
]

autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
branch = 'master'
language = 'en'
exclude_patterns = ['_build']
pygments_style = 'friendly'

# -- Options for HTML output ----------------------------------------------

html_theme = 'basic'

html_js_files = [
  'copy.js',
  'custom.js',
  'settings.js',
  'sidebar.js'
]
