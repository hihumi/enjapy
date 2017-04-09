#!/use/bin/env python3


"""assuranceの日本語意味を出力する
"""


def assurance_ja_func():
    """assuranceの日本語意味を出力する関数

    doctest:
    >>> assurance_ja_func()
    assurance:
        [名]: [加算, 不加算]: (1) 確約 (2) 保証
    """

    print('assurance:')

    assurance_ja_words = """    [名]: [加算, 不加算]: (1) 確約 (2) 保証"""

    print(assurance_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    assurance_ja_func()
