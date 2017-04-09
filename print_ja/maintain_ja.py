#!/use/bin/env python3


"""maintainの日本語意味を出力する
"""


def maintain_ja_func():
    """maintainの日本語意味を出力する関数

    doctest:
    >>> maintain_ja_func()
    maintain:
        [動]: (1) ...(関係等を)維持する (2) ...(機械等を)手入れする (3) ...と主張する
    """

    print('maintain:')

    maintain_ja_words = """    [動]: (1) ...(関係等を)維持する (2) ...(機械等を)手入れする (3) ...と主張する"""

    print(maintain_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    maintain_ja_func()
