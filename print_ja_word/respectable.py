#!/use/bin/env python3


"""respectableの日本語意味を出力する
"""

def respectable():
    """respectableの日本語意味を出力する関数

    doctest:
    >>> respectable()
    [形]: (1) (世間的・社会的に)まともな (2) (量等が)かなりの
    """

    respectable_ja = """[形]: (1) (世間的・社会的に)まともな (2) (量等が)かなりの"""

    print(respectable_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    respectable()
