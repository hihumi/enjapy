#!/use/bin/env python3


"""increaseの日本語意味を出力する
"""


def increase_ja_func():
    """increaseの日本語意味を出力する関数

    doctest:
    >>> increase_ja_func()
    increase:
    <BLANKLINE>
        [動] [自] 増える, 増加する, 増大する
        [他] ...を増やす, ...を強める, ...を上げる
    <BLANKLINE>
        [名] (1) [C,U] 増加, 増強, 上昇 (2) [C] 増加量, 増価額
    """

    print('increase:')
    print()

    increase_ja_words = """    [動] [自] 増える, 増加する, 増大する
    [他] ...を増やす, ...を強める, ...を上げる

    [名] (1) [C,U] 増加, 増強, 上昇 (2) [C] 増加量, 増価額"""

    print(increase_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    increase_ja_func()
