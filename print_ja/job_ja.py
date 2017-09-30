#!/use/bin/env python3


"""jobの日本語意味を出力する
"""


def job_ja_func():
    """jobの日本語意味を出力する関数

    doctest:
    >>> job_ja_func()
    job:
    <BLANKLINE>
        [名] [C] (1) 職, 仕事, 勤め口 (2) 責務, やるべきこと, すべきこと
    """

    print('job:')
    print('')

    job_ja_words = """    [名] [C] (1) 職, 仕事, 勤め口 (2) 責務, やるべきこと, すべきこと"""

    print(job_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    job_ja_func()
