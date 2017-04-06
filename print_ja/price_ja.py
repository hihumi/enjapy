#!/use/bin/env python3


"""priceの日本語意味を出力する
"""


def price_ja_func():
    """priceの日本語意味を出力する関数

    doctest:
    >>> price_ja_func()
    price:
    [名]: [加算, 不加算]: (1) 価格, 値段, 物価 (2) (単数形で)代償, 犠牲 (3) (人の首に掛かる)懸賞金 (4) (競馬等で)賭け率
    [動]: (...に)値段を付ける
    """

    print('price:')

    price_ja_words = """[名]: [加算, 不加算]: (1) 価格, 値段, 物価 (2) (単数形で)代償, 犠牲 (3) (人の首に掛かる)懸賞金 (4) (競馬等で)賭け率
[動]: (...に)値段を付ける"""

    print(price_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    price_ja_func()
