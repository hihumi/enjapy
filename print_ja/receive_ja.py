#!/use/bin/env python3


"""receiveの日本語意味を出力する
"""


def receive_ja_func():
    """receiveの日本語意味を出力する関数

    doctest:
    >>> receive_ja_func()
    receive:
    <BLANKLINE>
        [動] [自] ...を受け取る [他] 受け取る
    """

    print('receive:')
    print('')

    receive_ja_words = """    [動] [自] ...を受け取る [他] 受け取る"""

    print(receive_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    receive_ja_func()
