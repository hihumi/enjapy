#!/usr/bin/env python3


"""respectfulの正規表現をコンパイルする
"""


import re


def respectful_re_func():
    """respectfulの正規表現をコンパイルする関数

    return value: respectful_re

    doctest:
    >>> print(respectful_re_func())
    re.compile('respectful$', re.IGNORECASE)
    """

    respectful_re = re.compile(r'respectful$', re.I)
    return respectful_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(respectful_re_func())
