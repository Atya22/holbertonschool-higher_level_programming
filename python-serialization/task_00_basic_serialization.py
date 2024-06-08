#!/usr/bin/env python3

"""
This module 0.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Function to serialize and save data to file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Function to load and deserialize data from specified file
    """
    with open(filename, 'r') as f:
        return json.load(f)
