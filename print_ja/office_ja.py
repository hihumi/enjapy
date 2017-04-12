#!/use/bin/env python3


"""officeの日本語意味を出力する
"""


def office_ja_func():
    """officeの日本語意味を出力する関数

    doctest:
    >>> office_ja_func()
    office:
    <BLANKLINE>
        [名] [C,U] (1) 事務所 (2) 職場 (3) 役所 (4) 案内所
    """

    print('office:')
    print()

    office_ja_words = """    [名] [C,U] (1) 事務所 (2) 職場 (3) 役所 (4) 案内所"""

    print(office_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    office_ja_func()
