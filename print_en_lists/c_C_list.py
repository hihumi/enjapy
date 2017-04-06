#!/usr/bin/env python3


"""cまたはCから始まる英単語のリストを出力する
"""


def c_C_list_func():
    """cまたはCから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> c_C_list_func()
    call
    company
    """

    c_C_en_words = sorted(['call', 'company'])

    [print(i) for i in c_C_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    c_C_list_func()
