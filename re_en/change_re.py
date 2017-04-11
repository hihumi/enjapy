#!/usr/bin/env python3


"""changeの正規表現をコンパイルする
"""


import re


def change_re_func():
    """changeの正規表現をコンパイルする関数

    return value: change_re

    doctest:
    >>> print(change_re_func())
    re.compile('change$', re.IGNORECASE)
    """

    change_re = re.compile(r'change$', re.I)
    return change_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(change_re_func())
