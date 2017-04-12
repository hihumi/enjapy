#!/use/bin/env python3


"""marketの日本語意味を出力する
"""


def market_ja_func():
    """marketの日本語意味を出力する関数

    doctest:
    >>> market_ja_func()
    market:
    <BLANKLINE>
        [名] [C] (1) 市場 (2) 食料品店 (3) 取引, 売買
    <BLANKLINE>
        [動] [他] ...を市場に出す, 取引する [自] 市場で取引する, 買い物をする
    """

    print('market:')
    print()

    market_ja_words = """    [名] [C] (1) 市場 (2) 食料品店 (3) 取引, 売買

    [動] [他] ...を市場に出す, 取引する [自] 市場で取引する, 買い物をする"""

    print(market_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    market_ja_func()
