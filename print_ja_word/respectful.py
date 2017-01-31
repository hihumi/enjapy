#!/use/bin/env python3


"""respectfulの日本語意味を出力する
"""

def respectful():
    """respectfulの日本語意味を出力する関数

    doctest:
    >>> respectful()
    [形]敬意を示す・表す
    """

    respectful_ja = """[形]敬意を示す・表す"""

    print(respectful_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    respectful()
