#!/usr/bin/env python3


"""s-listの正規表現をコンパイルする
"""


import re


def s_S_list_re_func():
    """s-listの正規表現をコンパイルする関数

    return value: s_S_list_re

    doctest:
    >>> print(s_S_list_re_func())
    re.compile('s-list$', re.IGNORECASE)
    """

    s_S_list_re = re.compile(r's-list$', re.I)
    return s_S_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(s_S_list_re_func())
