#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
