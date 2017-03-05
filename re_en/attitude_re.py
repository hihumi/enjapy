#!/usr/bin/env python3


"""attitudeの正規表現をコンパイルする
"""


import re


def attitude_re_func():
    """attitudeの正規表現をコンパイルする関数

    return value: attitude_re

    doctest:
    >>> print(attitude_re_func())
    re.compile('attitude$', re.IGNORECASE)
    """

    attitude_re = re.compile(r'attitude$', re.I)
    return attitude_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(attitude_re_func())
