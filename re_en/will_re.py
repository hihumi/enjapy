#!/usr/bin/env python3


"""willの正規表現をコンパイルする
"""


import re


def will_re_func():
    """willの正規表現をコンパイルする関数

    return value: will_re

    doctest:
    >>> print(will_re_func())
    re.compile('^will$', re.IGNORECASE)
    """

    will_re = re.compile(r'^will$', re.I)
    return will_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(will_re_func())
