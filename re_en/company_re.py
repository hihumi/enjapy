#!/usr/bin/env python3


"""companyの正規表現をコンパイルする
"""


import re


def company_re_func():
    """companyの正規表現をコンパイルする関数

    return value: company_re

    doctest:
    >>> print(company_re_func())
    re.compile('^company$', re.IGNORECASE)
    """

    company_re = re.compile(r'^company$', re.I)
    return company_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(company_re_func())
