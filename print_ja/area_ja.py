#!/use/bin/env python3


"""areaの日本語意味を出力する
"""


def area_ja_func():
    """areaの日本語意味を出力する関数

    doctest:
    >>> area_ja_func()
    area:
    <BLANKLINE>
        [名] (1) [U,C] 面積, 坪数, 建坪 (2) [C] 地域, 地帯, 地方
        (3) [C] 広場, 空き地, 区域, 場所, 空間 (4) [C] 範囲, 分野, 領域
    """

    print('area:')
    print('')

    area_ja_words = """    [名] (1) [U,C] 面積, 坪数, 建坪 (2) [C] 地域, 地帯, 地方
    (3) [C] 広場, 空き地, 区域, 場所, 空間 (4) [C] 範囲, 分野, 領域"""

    print(area_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    area_ja_func()
