#!/use/bin/env python3


"""roomの日本語意味を出力する
"""


def room_ja_func():
    """roomの日本語意味を出力する関数

    doctest:
    >>> room_ja_func()
    room:
    <BLANKLINE>
        [名] [複 ~s] (1) [C] 部屋, 質 (2) [U] 空間, 場所,
        余地
        (3) [U] 可能性, 機会 (4) (複数形で)貸し室, 下宿
        (5) (the ~ (集合的に))部屋にいる人々, 集合した人々
    <BLANKLINE>
        [動] [自] 同居する, 下宿する, 間借りする
    """

    print('room:')
    print()

    room_ja_words = """    [名] [複 ~s] (1) [C] 部屋, 質 (2) [U] 空間, 場所,
    余地
    (3) [U] 可能性, 機会 (4) (複数形で)貸し室, 下宿
    (5) (the ~ (集合的に))部屋にいる人々, 集合した人々

    [動] [自] 同居する, 下宿する, 間借りする"""

    print(room_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    room_ja_func()
