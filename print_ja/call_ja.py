#!/use/bin/env python3


"""callの日本語意味を出力する
"""


def call_ja_func():
    """callの日本語意味を出力する関数

    doctest:
    >>> call_ja_func()
    call:
        [動] (1) 呼ぶ (2) 電話を掛ける
    <BLANKLINE>
        [名] [C] (1) 呼び出し (2) 通話
    """

    print('call:')

    call_ja_words = """    [動] (1) 呼ぶ (2) 電話を掛ける

    [名] [C] (1) 呼び出し (2) 通話"""

    print(call_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    call_ja_func()
