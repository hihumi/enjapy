#!/usr/bin/env python3


"""o-listの正規表現をコンパイルする
"""


import re


def o_O_list_re_func():
    """o-listの正規表現をコンパイルする関数

    return value: o_O_list_re

    doctest:
    >>> print(o_O_list_re_func())
    re.compile('o-list$', re.IGNORECASE)
    """

    o_O_list_re = re.compile(r'o-list$', re.I)
    return o_O_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(o_O_list_re_func())
