#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if chr(n) != 'e' and chr(n) != 'q':
        print('{:c}'.format(n), end='')
