#!/usr/bin/python3

def new_in_list(my_list, i, element):
    if 0 <= i < len(my_list):
        return my_list[:i] + [element] + my_list[i + 1:]
    else:
        return my_list
