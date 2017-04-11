#!/usr/bin/env python3


"""checkの正規表現をコンパイルする
"""


import re


def check_re_func():
    """checkの正規表現をコンパイルする関数

    return value: check_re

    doctest:
    >>> print(check_re_func())
    re.compile('^check$', re.IGNORECASE)
    """

    check_re = re.compile(r'^check$', re.I)
    return check_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(check_re_func())
