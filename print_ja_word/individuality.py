#!/use/bin/env python3


"""individualityの日本語意味を出力する
"""

def individuality():
    """individualityの日本語意味を出力する関数

    doctest:
    >>> individuality()
    [名]: [不加算]: 個性
    """

    individuality_ja = """[名]: [不加算]: 個性"""

    print(individuality_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    individuality()
