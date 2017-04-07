#!/usr/bin/env python3


"""i-listの正規表現をコンパイルする
"""


import re


def i_I_list_re_func():
    """i-listの正規表現をコンパイルする関数

    return value: i_I_list_re

    doctest:
    >>> print(i_I_list_re_func())
    re.compile('i-list$', re.IGNORECASE)
    """

    i_I_list_re = re.compile(r'i-list$', re.I)
    return i_I_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(i_I_list_re_func())
