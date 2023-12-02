#!/usr/bin/python3

def delete_at(my_list=[], i=0):
    if i < 0 or i >= len(my_list):
        return my_list
    new_list = my_list[:i] + my_list[i+1:]
    return new_list
