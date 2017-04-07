#!/usr/bin/env python3


"""bまたはBから始まる英単語のリストを出力する
"""


def b_B_list_func():
    """bまたはbから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> b_B_list_func()
    b-list:
        base
        business
    """

    print('b-list:')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    b_B_en_words = sorted(['business', 'base'])

    [print('    {}'.format(i)) for i in b_B_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    b_B_list_func()
