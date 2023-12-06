#!/usr/bin/python3

def weight_average(my_list=None):
    if my_list is None or not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    avg = 0
    weight = 0

    for x in my_list:
        if len(x) == 2:
            avg += x[0] * x[1]
            weight += x[1]

    if weight == 0:
        return 0
    
    return avg / weight
