#!/use/bin/env python3


"""respectableの日本語意味を出力する
"""

def respectable_ja_func():
    """respectableの日本語意味を出力する関数

    doctest:
    >>> respectable_ja_func()
    [形]: (1) (世間的・社会的に)まともな (2) (量等が)かなりの
    """

    respectable_ja_text = """[形]: (1) (世間的・社会的に)まともな (2) (量等が)かなりの"""

    print(respectable_ja_text)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    respectable_ja_func()
