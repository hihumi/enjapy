#!/use/bin/env python3


"""rateの日本語意味を出力する
"""


def rate_ja_func():
    """rateの日本語意味を出力する関数

    doctest:
    >>> rate_ja_func()
    rate:
    [名]: [加算]: (1) 割合, 比率 (2) 料金, 値段 (3) 速度
    [動]: ...を評価する
    """

    print('rate:')

    rate_ja_words = """[名]: [加算]: (1) 割合, 比率 (2) 料金, 値段 (3) 速度
[動]: ...を評価する"""

    print(rate_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    rate_ja_func()
