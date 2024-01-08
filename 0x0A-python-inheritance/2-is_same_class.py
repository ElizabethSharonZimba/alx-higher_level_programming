#!/usr/bin/python3
"""Defines a class-checking function"""

def is_same_classs(obj, a_class):
    """Checking if  an object is exactly an instance of a given class Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False."""
    if type(obj) == a_class:
        return True
    return False
