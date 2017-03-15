#!/usr/bin/env python3


"""serviceの正規表現をコンパイルする
"""


import re


def service_re_func():
    """serviceの正規表現をコンパイルする関数

    return value: service_re

    doctest:
    >>> print(service_re_func())
    re.compile('service$', re.IGNORECASE)
    """

    service_re = re.compile(r'service$', re.I)
    return service_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(service_re_func())
