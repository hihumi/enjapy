#!/usr/bin/env python3


"""increaseの正規表現をコンパイルする
"""


import re


def increase_re_func():
    """increaseの正規表現をコンパイルする関数

    return value: increase_re

    doctest:
    >>> print(increase_re_func())
    re.compile('^increase$', re.IGNORECASE)
    """

    increase_re = re.compile(r'^increase$', re.I)
    return increase_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(increase_re_func())
