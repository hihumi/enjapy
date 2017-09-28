#!/usr/bin/env python3


"""tまたはTから始まる英単語のリストを出力する
"""


def t_T_list_func():
    """tまたはtから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> t_T_list_func()
    t-list:
    <BLANKLINE>
        tax
    """

    print('t-list:')
    print('')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    t_T_en_words = sorted(['tax'])

    [print('    {}'.format(i)) for i in t_T_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    t_T_list_func()
