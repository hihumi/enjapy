#!/usr/bin/env python3


"""c-listの正規表現をコンパイルする
"""


import re


def c_C_list_re_func():
    """c-listの正規表現をコンパイルする関数

    return value: c_C_list_re

    doctest:
    >>> print(c_C_list_re_func())
    re.compile('^c-list$', re.IGNORECASE)
    """

    c_C_list_re = re.compile(r'^c-list$', re.I)
    return c_C_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(c_C_list_re_func())
