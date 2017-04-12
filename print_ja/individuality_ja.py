#!/use/bin/env python3


"""individualityの日本語意味を出力する
"""


def individuality_ja_func():
    """individualityの日本語意味を出力する関数

    doctest:
    >>> individuality_ja_func()
    individuality:
    <BLANKLINE>
        [名] [U] 個性
    """

    print('individuality:')
    print()

    individuality_ja_words = """    [名] [U] 個性"""

    print(individuality_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    individuality_ja_func()
