#!/use/bin/env python3


"""companyの日本語意味を出力する
"""


def company_ja_func():
    """companyの日本語意味を出力する関数

    doctest:
    >>> company_ja_func()
    company:
        [名]: [加算, 不加算]: (1) 会社 (2) 同席, 同行 (3) 仲間
    """

    print('company:')

    company_ja_words = """    [名]: [加算, 不加算]: (1) 会社 (2) 同席, 同行 (3) 仲間"""

    print(company_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    company_ja_func()
