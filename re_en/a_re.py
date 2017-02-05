#!/usr/bin/env python3


"""aの正規表現をコンパイルする
"""


import re


def a_re_func():
    """aの正規表現をコンパイルする関数

    return value: a_re

    doctest:
    >>> print(a_re_func())
    re.compile('a$', re.IGNORECASE)
    """

    a_re = re.compile(r'a$', re.I)
    return a_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(a_re_func())
