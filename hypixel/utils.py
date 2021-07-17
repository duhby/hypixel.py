"""
The MIT License (MIT)

Copyright (c) 2021-present duhby

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Dict

def _clean(data: Dict, mode=None) -> Dict:
    if mode is None:
        aliases = Constants.ALIASES
    else:
        aliases = Constants.GAMEMODES[mode]
    # replaces the keys in the data with their equivalent alias
    replaced_data = {aliases.get(k, k): v for k, v in data.items()}
    # removes unused keys
    return dict((key, replaced_data[key]) for key in [k for k in aliases.keys() if k in replaced_data])

def get_level(network_exp: int) -> float:
    return 1 + (-8750.0 + (8750 ** 2 + 5000 * network_exp) ** 0.5) / 2500
