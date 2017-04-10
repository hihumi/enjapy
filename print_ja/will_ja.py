#!/use/bin/env python3


"""willの日本語意味を出力する
"""


def will_ja_func():
    """willの日本語意味を出力する関数

    doctest:
    >>> will_ja_func()
    will:
        [名] [C,U] (1) 意志 (2) 遺書
    """

    print('will:')

    will_ja_words = """    [名] [C,U] (1) 意志 (2) 遺書"""

    print(will_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    will_ja_func()
