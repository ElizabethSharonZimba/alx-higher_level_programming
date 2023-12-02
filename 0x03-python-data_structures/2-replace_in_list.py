#!/usr/bin/python3

def replace_in_list(my_list, i, element):
    if i < 0:
        return my_list
    if i >= len(my_list):
        return my_list
    my_list[i] = element
    return my_list
