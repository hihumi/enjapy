#!/usr/bin/env python3


"""taxの正規表現をコンパイルする
"""


import re


def tax_re_func():
    """taxの正規表現をコンパイルする関数

    return value: tax_re

    doctest:
    >>> print(tax_re_func())
    re.compile('^tax$', re.IGNORECASE)
    """

    tax_re = re.compile(r'^tax$', re.I)
    return tax_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(tax_re_func())
