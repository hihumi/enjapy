#!/usr/bin/env python3


"""storeの正規表現をコンパイルする
"""


import re


def store_re_func():
    """storeの正規表現をコンパイルする関数

    return value: store_re

    doctest:
    >>> print(store_re_func())
    re.compile('store$', re.IGNORECASE)
    """

    store_re = re.compile(r'store$', re.I)
    return store_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(store_re_func())
