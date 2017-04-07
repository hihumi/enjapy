#!/usr/bin/env python3


"""marketの正規表現をコンパイルする
"""


import re


def market_re_func():
    """marketの正規表現をコンパイルする関数

    return value: market_re

    doctest:
    >>> print(market_re_func())
    re.compile('market$', re.IGNORECASE)
    """

    market_re = re.compile(r'market$', re.I)
    return market_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(market_re_func())
