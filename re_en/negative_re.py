#!/usr/bin/env python3


"""negativeの正規表現をコンパイルする
"""


import re


def negative_re_func():
    """negativeの正規表現をコンパイルする関数

    return value: negative_re

    doctest:
    >>> print(negative_re_func())
    re.compile('^negative$', re.IGNORECASE)
    """

    negative_re = re.compile(r'^negative$', re.I)
    return negative_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(negative_re_func())
