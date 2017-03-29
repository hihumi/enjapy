#!/usr/bin/env python3


"""businessの正規表現をコンパイルする
"""


import re


def business_re_func():
    """businessの正規表現をコンパイルする関数

    return value: business_re

    doctest:
    >>> print(business_re_func())
    re.compile('business$', re.IGNORECASE)
    """

    business_re = re.compile(r'business$', re.I)
    return business_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(business_re_func())
