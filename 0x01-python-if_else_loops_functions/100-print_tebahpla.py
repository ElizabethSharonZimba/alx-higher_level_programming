#!/usr/bin/python3
print("".join(["{:c}".format(c+32 if c % 2 else c) for c in range(97, 123)]), end="")

