#!/use/bin/env python3


"""reportの日本語意味を出力する
"""


def report_ja_func():
    """reportの日本語意味を出力する関数

    doctest:
    >>> report_ja_func()
    report:
    <BLANKLINE>
        [名] [C,U] (1) 報告 (2) 報道 (3) 噂, 風説
    <BLANKLINE>
        [動] (1) ...を報告する (2) ...を報道する
    """

    print('report:')
    print('')

    report_ja_words = """    [名] [C,U] (1) 報告 (2) 報道 (3) 噂, 風説

    [動] (1) ...を報告する (2) ...を報道する"""

    print(report_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    report_ja_func()
