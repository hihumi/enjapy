#!/usr/bin/env python3


"""payの正規表現をコンパイルする
"""


import re


def pay_re_func():
    """payの正規表現をコンパイルする関数

    return value: pay_re

    doctest:
    >>> print(pay_re_func())
    re.compile('pay$', re.IGNORECASE)
    """

    pay_re = re.compile(r'pay$', re.I)
    return pay_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(pay_re_func())
