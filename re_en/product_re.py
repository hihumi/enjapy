#!/usr/bin/env python3


"""productの正規表現をコンパイルする
"""


import re


def product_re_func():
    """productの正規表現をコンパイルする関数

    return value: product_re

    doctest:
    >>> print(product_re_func())
    re.compile('^product$', re.IGNORECASE)
    """

    product_re = re.compile(r'^product$', re.I)
    return product_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(product_re_func())
