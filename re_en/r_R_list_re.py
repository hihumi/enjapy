#!/usr/bin/env python3


"""r-listの正規表現をコンパイルする
"""


import re


def r_R_list_re_func():
    """r_R_listの正規表現をコンパイルする関数

    return value: r_R_list_re

    doctest:
    >>> print(r_R_list_re_func())
    re.compile('^r-list$', re.IGNORECASE)
    """

    r_R_list_re = re.compile(r'^r-list$', re.I)
    return r_R_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(r_R_list_re_func())
