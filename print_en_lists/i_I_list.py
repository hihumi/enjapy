#!/usr/bin/env python3


"""iまたはIから始まる英単語のリストを出力する
"""


def i_I_list_func():
    """iまたはIから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> i_I_list_func()
    i-list:
        individual
        individuality
    """

    print('i-list:')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    i_I_en_words = sorted(['individual', 'individuality'])

    [print('    {}'.format(i)) for i in i_I_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    i_I_list_func()
