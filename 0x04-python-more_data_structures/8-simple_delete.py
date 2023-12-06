#!/usr/bin/python3

def simple_delete(a_dictionary=None, key=""):
    if a_dictionary is None:
        a_dictionary = {}
    
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

