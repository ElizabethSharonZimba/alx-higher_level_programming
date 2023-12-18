#!/usr/bin/python3
import sys

def safe_function(fact, *args):
    try:
        resul = fact(*args)
        return (resul)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
