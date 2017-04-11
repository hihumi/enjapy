#!/usr/bin/env python3


"""reportの正規表現をコンパイルする
"""


import re


def report_re_func():
    """reportの正規表現をコンパイルする関数

    return value: report_re

    doctest:
    >>> print(report_re_func())
    re.compile('^report$', re.IGNORECASE)
    """

    report_re = re.compile(r'^report$', re.I)
    return report_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(report_re_func())
