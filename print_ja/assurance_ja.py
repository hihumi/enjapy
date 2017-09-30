#!/use/bin/env python3


"""assuranceの日本語意味を出力する
"""


def assurance_ja_func():
    """assuranceの日本語意味を出力する関数

    doctest:
    >>> assurance_ja_func()
    assurance:
    <BLANKLINE>
        [名] [C] (1) 確約 (2) 保証 [U] (1) 確信 (2) 自信
    """

    print('assurance:')
    print('')

    assurance_ja_words = """    [名] [C] (1) 確約 (2) 保証 [U] (1) 確信 (2) 自信"""

    print(assurance_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    assurance_ja_func()
