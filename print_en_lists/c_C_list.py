#!/usr/bin/env python3


"""cまたはCから始まる英単語のリストを出力する
"""


def c_C_list_func():
    """cまたはCから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> c_C_list_func()
    c-list:
    call
    check
    company
    """

    print('c-list:')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    c_C_en_words = sorted(['call', 'company', 'check'])

    [print(i) for i in c_C_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    c_C_list_func()
