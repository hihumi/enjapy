#!/usr/bin/env python3


"""callの正規表現をコンパイルする
"""


import re


def call_re_func():
    """callの正規表現をコンパイルする関数

    return value: call_re

    doctest:
    >>> print(call_re_func())
    re.compile('^call$', re.IGNORECASE)
    """

    call_re = re.compile(r'^call$', re.I)
    return call_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(call_re_func())
