#!/use/bin/env python3


"""problemの日本語意味を出力する
"""


def problem_ja_func():
    """problemの日本語意味を出力する関数

    doctest:
    >>> problem_ja_func()
    problem:
        [名]: [加算]: 問題, 課題, 厄介な物事
    """

    print('problem:')

    problem_ja_words = """    [名]: [加算]: 問題, 課題, 厄介な物事"""

    print(problem_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    problem_ja_func()
