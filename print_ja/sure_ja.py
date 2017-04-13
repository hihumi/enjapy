#!/use/bin/env python3


"""sureの日本語意味を出力する
"""


def sure_ja_func():
    """sureの日本語意味を出力する関数

    doctest:
    >>> sure_ja_func()
    sure:
    <BLANKLINE>
        [形] (1) ...を確信している (2) きっと...する
        (3) ...するように気をつける, ...するように注意する
        (4) 信頼できる (5) 確かな, 確実な
    """

    print('sure:')
    print()

    sure_ja_words = """    [形] (1) ...を確信している (2) きっと...する
    (3) ...するように気をつける, ...するように注意する
    (4) 信頼できる (5) 確かな, 確実な"""

    print(sure_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sure_ja_func()
