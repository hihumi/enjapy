#!/use/bin/env python3


"""respectの日本語意味を出力する
"""


def respect_ja_func():
    """respectの日本語意味を出力する関数

    doctest:
    >>> respect_ja_func()
    respect:
    <BLANKLINE>
        [動] (1) ...を尊重する (2) ...を尊敬する
    <BLANKLINE>
        [名] [U] 尊敬
    """

    print('respect:')
    print()

    respect_ja_words = """    [動] (1) ...を尊重する (2) ...を尊敬する

    [名] [U] 尊敬"""

    print(respect_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    respect_ja_func()
