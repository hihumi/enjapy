#!/usr/bin/env python3


"""wantの正規表現をコンパイルする
"""


import re


def want_re_func():
    """wantの正規表現をコンパイルする関数

    return value: want_re

    doctest:
    >>> print(want_re_func())
    re.compile('^want$', re.IGNORECASE)
    """

    want_re = re.compile(r'^want$', re.I)
    return want_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(want_re_func())
