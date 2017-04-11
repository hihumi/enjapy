#!/usr/bin/env python3


"""roomの正規表現をコンパイルする
"""


import re


def room_re_func():
    """roomの正規表現をコンパイルする関数

    return value: room_re

    doctest:
    >>> print(room_re_func())
    re.compile('^room$', re.IGNORECASE)
    """

    room_re = re.compile(r'^room$', re.I)
    return room_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(room_re_func())
