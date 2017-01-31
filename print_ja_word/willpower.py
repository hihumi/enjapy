#!/use/bin/env python3


"""willpowerの日本語意味を出力する
"""

def willpower():
    """willpowerの日本語意味を出力する関数

    doctest:
    >>> willpower()
    [名]: [不加算]: 意志力
    """

    willpower_ja = """[名]: [不加算]: 意志力"""

    print(willpower_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    willpower()
