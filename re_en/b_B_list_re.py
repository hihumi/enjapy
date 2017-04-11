#!/usr/bin/env python3


"""b-listの正規表現をコンパイルする
"""


import re


def b_B_list_re_func():
    """b-listの正規表現をコンパイルする関数

    return value: b_B_list_re

    doctest:
    >>> print(b_B_list_re_func())
    re.compile('^b-list$', re.IGNORECASE)
    """

    b_B_list_re = re.compile(r'^b-list$', re.I)
    return b_B_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(b_B_list_re_func())
