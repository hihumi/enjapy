#!/use/bin/env python3


"""willの日本語意味を出力する
"""


#変更
#file名: will_ja
#関数名: will_ja_func
#変数名: will_ja_text

def will_ja_func():
    """willの日本語意味を出力する関数

    doctest:
    >>> will_ja_func()
    [名]: (1) [加算・不加算]: 意志 (2) [加算]: 遺書
    """

    will_ja_words = """[名]: (1) [加算・不加算]: 意志 (2) [加算]: 遺書"""

    print(will_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    will_ja_func()
