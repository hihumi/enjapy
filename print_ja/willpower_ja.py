#!/use/bin/env python3


"""willpowerの日本語意味を出力する
"""


def willpower_ja_func():
    """willpowerの日本語意味を出力する関数

    doctest:
    >>> willpower_ja_func()
    willpower:
    <BLANKLINE>
        [名] [U] 意志力
    """

    print('willpower:')
    print()

    willpower_ja_words = """    [名] [U] 意志力"""

    print(willpower_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    willpower_ja_func()
