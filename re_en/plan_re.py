#!/usr/bin/env python3


"""planの正規表現をコンパイルする
"""


import re


def plan_re_func():
    """planの正規表現をコンパイルする関数

    return value: plan_re

    doctest:
    >>> print(plan_re_func())
    re.compile('^plan$', re.IGNORECASE)
    """

    plan_re = re.compile(r'^plan$', re.I)
    return plan_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(plan_re_func())
