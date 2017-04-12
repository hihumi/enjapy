#!/use/bin/env python3


"""payの日本語意味を出力する
"""


def pay_ja_func():
    """payの日本語意味を出力する関数

    doctest:
    >>> pay_ja_func()
    pay:
    <BLANKLINE>
        [動] (1) (金等)を支払う (2) (注意等)を払う
    <BLANKLINE>
        [名] [U] 給料, 報酬
    """

    print('pay:')
    print()

    pay_ja_words = """    [動] (1) (金等)を支払う (2) (注意等)を払う

    [名] [U] 給料, 報酬"""

    print(pay_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pay_ja_func()
