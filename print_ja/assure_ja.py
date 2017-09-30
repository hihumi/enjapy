#!/use/bin/env python3


"""assureの日本語意味を出力する
"""


def assure_ja_func():
    """assureの日本語意味を出力する関数

    doctest:
    >>> assure_ja_func()
    assure:
    <BLANKLINE>
        [動] (1) ...を確実にする (2) ...を保証する
    """

    print('assure:')
    print('')

    assure_ja_words = """    [動] (1) ...を確実にする (2) ...を保証する"""

    print(assure_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    assure_ja_func()
