#!/usr/bin/env python3


"""n-listの正規表現をコンパイルする
"""


import re


def n_N_list_re_func():
    """n-listの正規表現をコンパイルする関数

    return value: n_N_list_re

    doctest:
    >>> print(n_N_list_re_func())
    re.compile('^n-list$', re.IGNORECASE)
    """

    n_N_list_re = re.compile(r'^n-list$', re.I)
    return n_N_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(n_N_list_re_func())
