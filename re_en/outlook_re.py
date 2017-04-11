#!/usr/bin/env python3


"""outlookの正規表現をコンパイルする
"""


import re


def outlook_re_func():
    """outlookの正規表現をコンパイルする関数

    return value: outlook_re

    doctest:
    >>> print(outlook_re_func())
    re.compile('^outlook$', re.IGNORECASE)
    """

    outlook_re = re.compile(r'^outlook$', re.I)
    return outlook_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(outlook_re_func())
