#!/usr/bin/env python3


"""j-listの正規表現をコンパイルする
"""


import re


def j_J_list_re_func():
    """xxxの正規表現をコンパイルする関数

    return value: j_J_list_re

    doctest:
    >>> print(j_J_list_re_func())
    re.compile('^j-list$', re.IGNORECASE)
    """

    j_J_list_re = re.compile(r'^j-list$', re.I)
    return j_J_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(j_J_list_re_func())
