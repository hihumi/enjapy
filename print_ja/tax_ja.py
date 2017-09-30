#!/use/bin/env python3


"""taxの日本語意味を出力する
"""


def tax_ja_func():
    """taxの日本語意味を出力する関数

    doctest:
    >>> tax_ja_func()
    tax:
    <BLANKLINE>
        [名] [C,U] 税金
        [動] [他] ...に課税する
    """

    print('tax:')
    print('')

    tax_ja_words = """    [名] [C,U] 税金
    [動] [他] ...に課税する"""

    print(tax_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    tax_ja_func()
