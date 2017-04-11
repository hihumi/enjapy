#!/usr/bin/env python3


"""jobの正規表現をコンパイルする
"""


import re


def job_re_func():
    """jobの正規表現をコンパイルする関数

    return value: job_re

    doctest:
    >>> print(job_re_func())
    re.compile('^job$', re.IGNORECASE)
    """

    job_re = re.compile(r'^job$', re.I)
    return job_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(job_re_func())
