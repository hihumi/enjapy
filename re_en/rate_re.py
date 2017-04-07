#!/usr/bin/env python3


"""rateの正規表現をコンパイルする
"""


import re


def rate_re_func():
    """rateの正規表現をコンパイルする関数

    return value: rate_re

    doctest:
    >>> print(rate_re_func())
    re.compile('rate$', re.IGNORECASE)
    """

    rate_re = re.compile(r'rate$', re.I)
    return rate_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(rate_re_func())
