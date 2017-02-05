#!/use/bin/env python3


"""aの日本語意味を出力する(これはif-elif-elseの先頭のifに使うだけ)
"""

def a_ja_func():
    """aの日本語意味を出力する関数

    doctest:
    >>> a_ja_func()
    えい・えー
    """

    a_ja_words = """えい・えー"""

    print(a_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    a_ja_func()
