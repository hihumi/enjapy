#!/usr/bin/env python3


"""freeの正規表現をコンパイルする
"""


import re


def free_re_func():
    """freeの正規表現をコンパイルする関数

    return value: free_re

    doctest:
    >>> print(free_re_func())
    re.compile('free$', re.IGNORECASE)
    """

    free_re = re.compile(r'free$', re.I)
    return free_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(free_re_func())
