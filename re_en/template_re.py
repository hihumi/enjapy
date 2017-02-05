#!/usr/bin/env python3


"""xxxの正規表現をコンパイルする
"""


import re


def xxx_re_func():
    """xxxの正規表現をコンパイルする関数

    return value: xxx_re

    doctest:
    >>> print(xxx_re_func())
    re.compile('xxx$', re.IGNORECASE)
    """

    xxx_re = re.compile(r'xxx$', re.I)
    return xxx_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(xxx_re_func())
