#!/usr/bin/env python3


"""orderの正規表現をコンパイルする
"""


import re


def order_re_func():
    """orderの正規表現をコンパイルする関数

    return value: order_re

    doctest:
    >>> print(order_re_func())
    re.compile('^order$', re.IGNORECASE)
    """

    order_re = re.compile(r'^order$', re.I)
    return order_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(order_re_func())
