#!/use/bin/env python3


"""problemの日本語意味を出力する
"""


def problem_ja_func():
    """problemの日本語意味を出力する関数

    doctest:
    >>> problem_ja_func()
    problem:
    <BLANKLINE>
        [名] [C] 問題, 課題, 厄介な物事
    """

    print('problem:')
    print()

    problem_ja_words = """    [名] [C] 問題, 課題, 厄介な物事"""

    print(problem_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    problem_ja_func()
