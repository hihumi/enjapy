#!/use/bin/env python3


"""outlookの日本語意味を出力する
"""


def outlook_ja_func():
    """outlookの日本語意味を出力する関数

    doctest:
    >>> outlook_ja_func()
    outlook:
    <BLANKLINE>
        [名] [C] (1) 見方 (2) 見通し
    """

    print('outlook:')
    print()

    outlook_ja_words = """    [名] [C] (1) 見方 (2) 見通し"""

    print(outlook_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    outlook_ja_func()
