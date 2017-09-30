#!/use/bin/env python3


"""changeの日本語意味を出力する
"""


def change_ja_func():
    """changeの日本語意味を出力する関数

    doctest:
    >>> change_ja_func()
    change:
    <BLANKLINE>
        [動] [他] (1) ...を変える, ...を変更する
        (2) ...を取り替える, ...を交換する (3) (お金を)両替する
        [自] (1) 変わる, 変化する (2) (衣服等を)着替える (3) 交換する
    <BLANKLINE>
        [名] (1) [U,C] 変化, 修正, 変遷 (2) [C] 交換, 変更, 乗り換え
        (3) [U] 釣り銭 [U] 小銭
    """

    print('change:')
    print('')

    change_ja_words = """    [動] [他] (1) ...を変える, ...を変更する
    (2) ...を取り替える, ...を交換する (3) (お金を)両替する
    [自] (1) 変わる, 変化する (2) (衣服等を)着替える (3) 交換する

    [名] (1) [U,C] 変化, 修正, 変遷 (2) [C] 交換, 変更, 乗り換え
    (3) [U] 釣り銭 [U] 小銭"""

    print(change_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    change_ja_func()
