#!/usr/bin/env python3


"""positiveの正規表現をコンパイルする
"""


import re


def positive_re_func():
    """positiveの正規表現をコンパイルする関数

    return value: positive_re

    doctest:
    >>> print(positive_re_func())
    re.compile('^positive$', re.IGNORECASE)
    """

    positive_re = re.compile(r'^positive$', re.I)
    return positive_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(positive_re_func())
