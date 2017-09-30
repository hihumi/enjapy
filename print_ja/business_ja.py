#!/use/bin/env python3


"""businessの日本語意味を出力する
"""


def business_ja_func():
    """businessの日本語意味を出力する関数

    doctest:
    >>> business_ja_func()
    business:
    <BLANKLINE>
        [名] [C,U] (1) 商売, 事業 (2) 物事
    """

    print('business:')
    print('')

    business_ja_words = """    [名] [C,U] (1) 商売, 事業 (2) 物事"""

    print(business_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    business_ja_func()
