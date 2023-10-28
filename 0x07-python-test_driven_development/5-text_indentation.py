#!/usr/bin/python3

"""
This is a module that contain text_indentation function

text_indentation = __import__('5-text_indentation').text_indentation
text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
"""

def text_indentation(text):
    """
    this function prints text and replace ['.', '?', ':'] with newline
    para:
        text - the main para
    print(edited_text)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
