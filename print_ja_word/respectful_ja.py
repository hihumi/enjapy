#!/use/bin/env python3


"""respectfulの日本語意味を出力する
"""

def respectful_ja_func():
    """respectfulの日本語意味を出力する関数

    doctest:
    >>> respectful_ja_func()
    [形]: 敬意を示す・表す
    """

    respectful_ja_words = """[形]: 敬意を示す・表す"""

    print(respectful_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    respectful_ja_func()
