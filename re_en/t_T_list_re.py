#!/usr/bin/env python3


"""t-listの正規表現をコンパイルする
"""


import re


def t_T_list_re_func():
    """t-listの正規表現をコンパイルする関数

    return value: t_T_list_re

    doctest:
    >>> print(t_T_list_re_func())
    re.compile('^t-list$', re.IGNORECASE)
    """

    t_T_list_re = re.compile(r'^t-list$', re.I)
    return t_T_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(t_T_list_re_func())
