#!/use/bin/env python3


"""wayの日本語意味を出力する
"""


def way_ja_func():
    """wayの日本語意味を出力する関数

    doctest:
    >>> way_ja_func()
    way:
    [名]: [加算, 不加算]: (1) (...の)やり方, (...を)する方法 (2) 道 (3) 方向
    """

    print('way:')

    way_ja_words = """[名]: [加算, 不加算]: (1) (...の)やり方, (...を)する方法 (2) 道 (3) 方向"""

    print(way_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    way_ja_func()
