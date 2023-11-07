#!/usr/bin/python3
"""Module 6-load_from_json_file.
        Creates an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """Creates an object from filename.
    Args:
        ...
    """

    with open(filename, 'r') as f:
        return json.load(f)
