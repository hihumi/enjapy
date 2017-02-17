#!/usr/bin/env python3


"""maintainの正規表現をコンパイルする
"""


import re


def maintain_re_func():
    """maintainの正規表現をコンパイルする関数

    return value: maintain_re

    doctest:
    >>> print(maintain_re_func())
    re.compile('maintain$', re.IGNORECASE)
    """

    maintain_re = re.compile(r'maintain$', re.I)
    return maintain_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(maintain_re_func())
