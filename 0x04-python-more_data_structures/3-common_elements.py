#!/usr/bin/python3

def common_elements(set_1=None, set_2=None):
    if set_1 is None:
        set_1 = set()
    if set_2 is None:
        set_2 = set()

    return set_1 & set_2
