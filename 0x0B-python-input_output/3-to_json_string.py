#!/usr/bin/python3
"""This module 
    Write a function that returns the JSON
"""
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object"""
    return json.dumbs(my_obj)
