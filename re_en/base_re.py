#!/usr/bin/env python3


"""baseの正規表現をコンパイルする
"""


import re


def base_re_func():
    """baseの正規表現をコンパイルする関数

    return value: base_re

    doctest:
    >>> print(base_re_func())
    re.compile('^base$', re.IGNORECASE)
    """

    base_re = re.compile(r'^base$', re.I)
    return base_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(base_re_func())
