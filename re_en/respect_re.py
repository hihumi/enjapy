#!/usr/bin/env python3


"""respectの正規表現をコンパイルする
"""


import re


def respect_re_func():
    """respectの正規表現をコンパイルする関数

    return value: respect_re

    doctest:
    >>> print(respect_re_func())
    re.compile('respect$', re.IGNORECASE)
    """

    respect_re = re.compile(r'respect$', re.I)
    return respect_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(respect_re_func())
