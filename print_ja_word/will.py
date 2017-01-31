#!/use/bin/env python3


"""willの日本語意味を出力する
"""

def will():
    """willの日本語意味を出力する関数

    doctest:
    >>> will()
    [名]: (1) [加算・不加算]: 意志 (2) [加算]: 遺書
    """

    will_ja = """[名]: (1) [加算・不加算]: 意志 (2) [加算]: 遺書"""

    print(will_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    will()
