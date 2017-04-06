#!/usr/bin/env python3


"""priceの正規表現をコンパイルする
"""


import re


def price_re_func():
    """priceの正規表現をコンパイルする関数

    return value: price_re

    doctest:
    >>> print(price_re_func())
    re.compile('price$', re.IGNORECASE)
    """

    price_re = re.compile(r'price$', re.I)
    return price_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(price_re_func())
