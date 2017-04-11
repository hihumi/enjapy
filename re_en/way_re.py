#!/usr/bin/env python3


"""wayの正規表現をコンパイルする
"""


import re


def way_re_func():
    """wayの正規表現をコンパイルする関数

    return value: way_re

    doctest:
    >>> print(way_re_func())
    re.compile('^way$', re.IGNORECASE)
    """

    way_re = re.compile(r'^way$', re.I)
    return way_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(way_re_func())
