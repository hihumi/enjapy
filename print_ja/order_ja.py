#!/use/bin/env python3


"""orderの日本語意味を出力する
"""


def order_ja_func():
    """orderの日本語意味を出力する関数

    doctest:
    >>> order_ja_func()
    order:
        [名]: [加算]: (1) 注文 (2) 命令 [不加算]: (1) 秩序 (2) 順序
    <BLANKLINE>
        [動]: (1) (モノ等)を注文する (2) ...を命令する
    """

    print('order:')

    order_ja_words = """    [名]: [加算]: (1) 注文 (2) 命令 [不加算]: (1) 秩序 (2) 順序

    [動]: (1) (モノ等)を注文する (2) ...を命令する"""

    print(order_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    order_ja_func()
