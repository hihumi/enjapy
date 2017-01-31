#!/use/bin/env python3


"""respectの日本語意味を出力する
"""

def respect():
    """respectの日本語意味を出力する関数

    doctest:
    >>> respect()
    [動]: (1) ...を尊重する (2) ...を尊敬する
    [名]: [不可算]: (1) 尊敬
    """

    respect_ja = """[動]: (1) ...を尊重する (2) ...を尊敬する
[名]: [不可算]: (1) 尊敬"""

    print(respect_ja)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    respect()
