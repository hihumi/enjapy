#!/usr/bin/env python3


"""saleの正規表現をコンパイルする
"""


import re


def sale_re_func():
    """saleの正規表現をコンパイルする関数

    return value: sale_re

    doctest:
    >>> print(sale_re_func())
    re.compile('^sale$', re.IGNORECASE)
    """

    sale_re = re.compile(r'^sale$', re.I)
    return sale_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(sale_re_func())
