#!/usr/bin/env python3


"""individualityの正規表現をコンパイルする
"""


import re


def individuality_re_func():
    """individualityの正規表現をコンパイルする関数

    return value: individuality_re

    doctest:
    >>> print(individuality_re_func())
    re.compile('individuality$', re.IGNORECASE)
    """

    individuality_re = re.compile(r'individuality$', re.I)
    return individuality_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(individuality_re_func())
