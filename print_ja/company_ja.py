#!/use/bin/env python3


"""companyの日本語意味を出力する
"""


def company_ja_func():
    """companyの日本語意味を出力する関数

    doctest:
    >>> company_ja_func()
    company:
    [名]: [加算]: 会社 [不加算]: 同席, 同行 [加算]: 仲間
    """

    print('company:')

    company_ja_words = """[名]: [加算]: 会社 [不加算]: 同席, 同行 [加算]: 仲間"""

    print(company_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    company_ja_func()
