#!/usr/bin/env python3


"""problemの正規表現をコンパイルする
"""


import re


def problem_re_func():
    """problemの正規表現をコンパイルする関数

    return value: problem_re

    doctest:
    >>> print(problem_re_func())
    re.compile('problem$', re.IGNORECASE)
    """

    problem_re = re.compile(r'problem$', re.I)
    return problem_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(problem_re_func())
