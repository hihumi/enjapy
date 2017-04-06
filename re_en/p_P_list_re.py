#!/usr/bin/env python3


"""p-listの正規表現をコンパイルする
"""


import re


def p_P_list_re_func():
    """xxxの正規表現をコンパイルする関数

    return value: p_P_list_re

    doctest:
    >>> print(p_P_list_re_func())
    re.compile('p-list$', re.IGNORECASE)
    """

    p_P_list_re = re.compile(r'p-list$', re.I)
    return p_P_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(p_P_list_re_func())
