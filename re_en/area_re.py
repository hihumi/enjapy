#!/usr/bin/env python3


"""areaの正規表現をコンパイルする
"""


import re


def area_re_func():
    """areaの正規表現をコンパイルする関数

    return value: area_re

    doctest:
    >>> print(area_re_func())
    re.compile('^area$', re.IGNORECASE)
    """

    area_re = re.compile(r'^area$', re.I)
    return area_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(area_re_func())
