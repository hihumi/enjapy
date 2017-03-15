#!/use/bin/env python3


"""serviceの日本語意味を出力する
"""


def service_ja_func():
    """serviceの日本語意味を出力する関数

    doctest:
    >>> service_ja_func()
    service:
    [名]: [加算, 不加算]: (1) 接客, サービス (2) (公共等の)事業
    """

    print('service:')

    service_ja_words = """[名]: [加算, 不加算]: (1) 接客, サービス (2) (公共等の)事業"""

    print(service_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    service_ja_func()
