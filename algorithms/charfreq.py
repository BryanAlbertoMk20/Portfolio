#!/usr/bin/env python3

# function that checks the frequency of the characters in a file.

def character_frequency(filename):
    """Counts the frequency of characters in a file."""
    # Open the file
    try:
        file = open(filename)
    except OSError:
        return None

    # Process the file.
    characters = {}
    for line in file:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    file.close()
    return characters

