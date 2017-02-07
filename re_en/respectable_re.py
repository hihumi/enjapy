#!/usr/bin/env python3


"""respectableの正規表現をコンパイルする
"""


import re


def respectable_re_func():
    """respectableの正規表現をコンパイルする関数

    return value: respectable_re

    doctest:
    >>> print(respectable_re_func())
    re.compile('respectable$', re.IGNORECASE)
    """

    respectable_re = re.compile(r'respectable$', re.I)
    return respectable_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(respectable_re_func())
