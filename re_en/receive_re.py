#!/usr/bin/env python3


"""receiveの正規表現をコンパイルする
"""


import re


def receive_re_func():
    """receiveの正規表現をコンパイルする関数

    return value: receive_re

    doctest:
    >>> print(receive_re_func())
    re.compile('^receive$', re.IGNORECASE)
    """

    receive_re = re.compile(r'^receive$', re.I)
    return receive_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(receive_re_func())
