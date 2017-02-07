#!/usr/bin/env python3


"""willpowerの正規表現をコンパイルする
"""


import re


def willpower_re_func():
    """willpowerの正規表現をコンパイルする関数

    return value: willpower_re

    doctest:
    >>> print(willpower_re_func())
    re.compile('willpower$', re.IGNORECASE)
    """

    willpower_re = re.compile(r'willpower$', re.I)
    return willpower_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(willpower_re_func())
