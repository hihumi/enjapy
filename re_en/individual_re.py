#!/usr/bin/env python3


"""individualの正規表現をコンパイルする
"""


import re


def individual_re_func():
    """individualの正規表現をコンパイルする関数

    return value: individual_re

    doctest:
    >>> print(individual_re_func())
    re.compile('individual$', re.IGNORECASE)
    """

    individual_re = re.compile(r'individual$', re.I)
    return individual_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(individual_re_func())
