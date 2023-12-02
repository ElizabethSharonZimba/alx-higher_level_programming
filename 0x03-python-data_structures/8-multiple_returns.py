#!/usr/bin/python3

def multiple_returns(sentence):
    sen_len = len(sentence) if sentence else 0
    first_char = sentence[:1] if sentence else None
    return sen_len, first_char
