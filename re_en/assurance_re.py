#!/usr/bin/env python3


"""assuranceの正規表現をコンパイルする
"""


import re


def assurance_re_func():
    """assuranceの正規表現をコンパイルする関数

    return value: assurance_re

    doctest:
    >>> print(assurance_re_func())
    re.compile('assurance$', re.IGNORECASE)
    """

    assurance_re = re.compile(r'assurance$', re.I)
    return assurance_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(assurance_re_func())
