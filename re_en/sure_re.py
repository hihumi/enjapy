#!/usr/bin/env python3


"""sureの正規表現をコンパイルする
"""


import re


def sure_re_func():
    """sureの正規表現をコンパイルする関数

    return value: sure_re

    doctest:
    >>> print(sure_re_func())
    re.compile('^sure$', re.IGNORECASE)
    """

    sure_re = re.compile(r'^sure$', re.I)
    return sure_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(sure_re_func())
