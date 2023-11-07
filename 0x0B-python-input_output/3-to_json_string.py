#!/usr/bin/python3
"""This module
    Write a function that returns the JSON
"""
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object
    Args:
        - my_obj: string to represent
    Returns: JSON representation
    """
    return json.dumps(my_obj)
