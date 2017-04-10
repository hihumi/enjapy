#!/use/bin/env python3


"""baseの日本語意味を出力する
"""


def base_ja_func():
    """baseの日本語意味を出力する関数

    doctest:
    >>> base_ja_func()
    base:
        [名] [C,U] 基部, 基礎, 土台, 底, 基地, 塁
        (備考: 基地, 塁として使用する場合, 不加算になることがある)
    <BLANKLINE>
        [動] (be ~d onで)...に基づいている
    """

    print('base:')

    base_ja_words = """    [名] [C,U] 基部, 基礎, 土台, 底, 基地, 塁
    (備考: 基地, 塁として使用する場合, 不加算になることがある)

    [動] (be ~d onで)...に基づいている"""

    print(base_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    base_ja_func()
