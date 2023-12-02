#!/usr/bin/python3

def no_c(my_string):
    my_string_list = list(my_string)
    for i, char in enumerate(my_string_list):
        if char.lower() == 'c':
            my_string_list[i] = ""
    return "".join(my_string_list)
