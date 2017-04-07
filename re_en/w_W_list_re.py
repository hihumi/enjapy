#!/usr/bin/env python3


"""w-listの正規表現をコンパイルする
"""


import re


def w_W_list_re_func():
    """w-listの正規表現をコンパイルする関数

    return value: w_W_list_re

    doctest:
    >>> print(w_W_list_re_func())
    re.compile('w-list$', re.IGNORECASE)
    """

    w_W_list_re = re.compile(r'w-list$', re.I)
    return w_W_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(w_W_list_re_func())
