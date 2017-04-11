#!/usr/bin/env python3


"""f-listの正規表現をコンパイルする
"""


import re


def f_F_list_re_func():
    """xxxの正規表現をコンパイルする関数

    return value: f_F_re

    doctest:
    >>> print(f_F_list_re_func())
    re.compile('f-list$', re.IGNORECASE)
    """

    f_F_list_re = re.compile(r'f-list$', re.I)
    return f_F_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(f_F_list_re_func())
