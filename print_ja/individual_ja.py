#!/use/bin/env python3


"""individualの日本語意味を出力する
"""


def individual_ja_func():
    """individualの日本語意味を出力する関数

    doctest:
    >>> individual_ja_func()
    individual:
        [名] [C] 個人
    <BLANKLINE>
        [形] (1) 個人の (2) 個々の (3) 個性的な
    """

    print('individual:')

    individual_ja_words = """    [名] [C] 個人

    [形] (1) 個人の (2) 個々の (3) 個性的な"""

    print(individual_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    individual_ja_func()
