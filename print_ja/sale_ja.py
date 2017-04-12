#!/use/bin/env python3


"""saleの日本語意味を出力する
"""


def sale_ja_func():
    """saleの日本語意味を出力する関数

    doctest:
    >>> sale_ja_func()
    sale:
    <BLANKLINE>
        [名] [複 ~s] (1) [U,C] 販売, 売却 (2) [U,C] [通例 ~s] 売り上げ高
        (3) [C] 特売 (4) [C] 競売
    """

    print('sale:')
    print()

    sale_ja_words = """    [名] [複 ~s] (1) [U,C] 販売, 売却 (2) [U,C] [通例 ~s] 売り上げ高
    (3) [C] 特売 (4) [C] 競売"""

    print(sale_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sale_ja_func()
