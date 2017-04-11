#!/usr/bin/env python3


"""officeの正規表現をコンパイルする
"""


import re


def office_re_func():
    """officeの正規表現をコンパイルする関数

    return value: office_re

    doctest:
    >>> print(office_re_func())
    re.compile('^office$', re.IGNORECASE)
    """

    office_re = re.compile(r'^office$', re.I)
    return office_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(office_re_func())
