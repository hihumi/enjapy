#!/usr/bin/env python3


"""assureの正規表現をコンパイルする
"""


import re


def assure_re_func():
    """assureの正規表現をコンパイルする関数

    return value: assure_re

    doctest:
    >>> print(assure_re_func())
    re.compile('assure$', re.IGNORECASE)
    """

    assure_re = re.compile(r'assure$', re.I)
    return assure_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(assure_re_func())
