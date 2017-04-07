#!/usr/bin/env python3


"""m_M_listの正規表現をコンパイルする
"""


import re


def m_M_list_re_func():
    """m_M_listの正規表現をコンパイルする関数

    return value: m_M_list_re

    doctest:
    >>> print(m_M_list_re_func())
    re.compile('m-list$', re.IGNORECASE)
    """

    m_M_list_re = re.compile(r'm-list$', re.I)
    return m_M_list_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(m_M_list_re_func())
