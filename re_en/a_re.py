#!/usr/bin/env python3


"""aの正規表現をコンパイルする
"""


import re

# from print_ja.a_ja import a_ja_func
# from re_en.re_search_en import re_search_en_func


def a_re_func():
    """aの正規表現をコンパイルする関数

    return value: a_re

    doctest:
    >>> print(a_re_func())
    re.compile('^a$', re.IGNORECASE)
    """

    #word2 = re_search_en_func(word)
    a_re = re.compile(r'^a$', re.I)
    # if a_re.search(word):
    #    print('#')
    #    a_ja_func()
    # else:
    #    print('not...')

    return a_re

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(a_re_func())
