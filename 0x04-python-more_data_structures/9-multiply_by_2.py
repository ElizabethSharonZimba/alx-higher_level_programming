#!/usr/bin/python3

def multiply_by_2(a_dictionary=None):
    if a_dictionary is None:
        a_dictionary = {}
    
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict

