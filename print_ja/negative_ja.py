#!/use/bin/env python3


"""negativeの日本語意味を出力する
"""


def negative_ja_func():
    """negativeの日本語意味を出力する関数

    doctest:
    >>> negative_ja_func()
    negative:
    [形]: (1) 悲観的な (2) 消極的な (3) 否定の (4) 陰性の
    [名]: [加算]: (1) ネガ (2) 否定
    """

    print('negative:')

    negative_ja_words = """[形]: (1) 悲観的な (2) 消極的な (3) 否定の (4) 陰性の
[名]: [加算]: (1) ネガ (2) 否定"""

    print(negative_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    negative_ja_func()
