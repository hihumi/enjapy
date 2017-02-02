#!/use/bin/env python3


"""aの日本語意味を出力する(これはif-elif-elseの先頭のifに使うだけ)
"""

def a():
    """aの日本語意味を出力する関数

    doctest:
    >>> a()
    a
    """

    a_ja = """a"""

    print(a_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    a()
