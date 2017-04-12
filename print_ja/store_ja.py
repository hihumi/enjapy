#!/use/bin/env python3


"""storeの日本語意味を出力する
"""


def store_ja_func():
    """storeの日本語意味を出力する関数

    doctest:
    >>> store_ja_func()
    store:
    <BLANKLINE>
        [名] [C] (1) 店, 商店 (2) 蓄え, 備え
    <BLANKLINE>
        [動] (1) ...を蓄える (2) ...を格納する (3) ...を貯蔵する
    """

    print('store:')
    print()

    store_ja_words = """    [名] [C] (1) 店, 商店 (2) 蓄え, 備え

    [動] (1) ...を蓄える (2) ...を格納する (3) ...を貯蔵する"""

    print(store_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    store_ja_func()
