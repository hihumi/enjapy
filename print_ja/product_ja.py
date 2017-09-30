#!/use/bin/env python3


"""productの日本語意味を出力する
"""


def product_ja_func():
    """productの日本語意味を出力する関数

    doctest:
    >>> product_ja_func()
    product:
    <BLANKLINE>
        [名] [C] (1) 製品, 生産物, 産出物, 創作品
        (2) 成果, 結果, 所産
        (3) (化学の)生成物
        (4) (数学の)積
    """

    print('product:')
    print('')

    product_ja_words = """    [名] [C] (1) 製品, 生産物, 産出物, 創作品
    (2) 成果, 結果, 所産
    (3) (化学の)生成物
    (4) (数学の)積"""

    print(product_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    product_ja_func()
