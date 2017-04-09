#!/use/bin/env python3


"""partの日本語意味を出力する
"""


def part_ja_func():
    """partの日本語意味を出力する関数

    doctest:
    >>> part_ja_func()
    part:
        [名]: [加算, 不加算]: (1) 部分 (2) 一部, 多少 (3) (しばしば複数形で)部品
        (4) 役割, 役 (5) 関わり, 参加 (6) (しばしば複数形で)地域, 区域
        (7) 部, 編 (8) 片側, 立場 (9) (演奏等の)パート (10) (しばしば複数形で)能力
    <BLANKLINE>
        [動]: [他]: (1) ...を分ける, ...を分割する (2) ...を切り離す, ...を区別する (3) ...を開ける
        [自]: (1) 分かれる (2) 避ける (3) (人等が)別れる (4) (物等が)外れる
    <BLANKLINE>
        [副]: 一部は, 部分的に
    <BLANKLINE>
        [形]: 一部分の
    """

    print('part:')

    part_ja_words = """    [名]: [加算, 不加算]: (1) 部分 (2) 一部, 多少 (3) (しばしば複数形で)部品
    (4) 役割, 役 (5) 関わり, 参加 (6) (しばしば複数形で)地域, 区域
    (7) 部, 編 (8) 片側, 立場 (9) (演奏等の)パート (10) (しばしば複数形で)能力

    [動]: [他]: (1) ...を分ける, ...を分割する (2) ...を切り離す, ...を区別する (3) ...を開ける
    [自]: (1) 分かれる (2) 避ける (3) (人等が)別れる (4) (物等が)外れる

    [副]: 一部は, 部分的に

    [形]: 一部分の"""

    print(part_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    part_ja_func()
