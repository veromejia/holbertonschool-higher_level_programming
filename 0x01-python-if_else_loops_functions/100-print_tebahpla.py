#!/usr/bin/python3
for letter in reversed(range(ord('a'), ord('z')+1)):
    if letter % 2:
        print(str.upper(chr(letter)), end='')
    else:
        print('{}'.format(chr(letter)), end='')
