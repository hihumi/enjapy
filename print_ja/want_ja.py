#!/use/bin/env python3


"""wantの日本語意味を出力する
"""


def want_ja_func():
    """wantの日本語意味を出力する関数

    doctest:
    >>> want_ja_func()
    want:
        [動] (1) ...を望む (2) ...が欠けている
    <BLANKLINE>
        [名] [C,U]: 欠乏
    """

    print('want:')

    want_ja_words = """    [動] (1) ...を望む (2) ...が欠けている

    [名] [C,U]: 欠乏"""

    print(want_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    want_ja_func()
