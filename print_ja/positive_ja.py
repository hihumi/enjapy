#!/use/bin/env python3


"""positiveの日本語意味を出力する
"""


def positive_ja_func():
    """positiveの日本語意味を出力する関数

    doctest:
    >>> positive_ja_func()
    positive:
        [形]: (1) 積極的な, 楽観的な (2) 確信, 自信のある (3) 明確な, 確実な
    """

    print('positive:')

    positive_ja_words = """    [形]: (1) 積極的な, 楽観的な (2) 確信, 自信のある (3) 明確な, 確実な"""

    print(positive_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    positive_ja_func()
