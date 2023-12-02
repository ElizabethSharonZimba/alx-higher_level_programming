#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        sen_len = 0
        first_char = None
    else:
        sen_len = len(sentence)
        first_char = sentence[:1] if sentence else None

    return sen_len, first_char
