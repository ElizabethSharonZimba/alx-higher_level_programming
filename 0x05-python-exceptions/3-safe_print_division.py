#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divi = a / b
    except (TypeError, ZeroDivisionError):
        divi = None
    finally:
        print("Inside result: {}".format(div))
    return (divi)
