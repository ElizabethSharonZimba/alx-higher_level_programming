#!/usr/bin/python3

def search_replace(my_list=None, search=None, replace=None):
    if my_list is None:
        my_list = []
    if search is None:
        search = []
    if replace is None:
        replace = []

    return [replace if x == search else x for x in my_list]
