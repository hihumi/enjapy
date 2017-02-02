#!/use/bin/env python3


"""individualの日本語意味を出力する
"""

def individual():
    """individualの日本語意味を出力する関数

    doctest:
    >>> individual()
    [名]: [加算]: 個人
    [形]: (1) 個人の (2) 個々の (3) 個性的な
    """

    individual_ja = """[名]: [加算]: 個人
[形]: (1) 個人の (2) 個々の (3) 個性的な"""

    print(individual_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    individual()
