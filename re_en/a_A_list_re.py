#!/usr/bin/env python3


"""a-listの正規表現をコンパイルする
"""


import re


def a_A_list_re_func():
    """a-listの正規表現をコンパイルする関数

    return value: a_A_list_re

    doctest:
    >>> print(a_A_list_re_func())
    re.compile('a-list$', re.IGNORECASE)
    """

    a_A_list_re = re.compile(r'a-list$', re.I)
    return a_A_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(a_A_list_re_func())
