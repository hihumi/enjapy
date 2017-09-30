#!/use/bin/env python3


"""attitudeの日本語意味を出力する
"""


def attitude_ja_func():
    """attitudeの日本語意味を出力する関数

    doctest:
    >>> attitude_ja_func()
    attitude:
    <BLANKLINE>
        [名] [C,U] (1) 態度 (2) 姿勢
    """

    print('attitude:')
    print('')

    attitude_ja_words = """    [名] [C,U] (1) 態度 (2) 姿勢"""

    print(attitude_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    attitude_ja_func()
