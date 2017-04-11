#!/usr/bin/env python3


"""fまたはFから始まる英単語のリストを出力する
"""


def f_F_list_func():
    """fまたはfから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> f_F_list_func()
    f-list:
        free
    """

    print('f-list:')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    f_F_en_words = sorted(['free'])

    [print('    {}'.format(i)) for i in f_F_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    f_F_list_func()
