#!/usr/bin/env python3


"""partの正規表現をコンパイルする
"""


import re


def part_re_func():
    """partの正規表現をコンパイルする関数

    return value: part_re

    doctest:
    >>> print(part_re_func())
    re.compile('part$', re.IGNORECASE)
    """

    part_re = re.compile(r'part$', re.I)
    return part_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(part_re_func())
