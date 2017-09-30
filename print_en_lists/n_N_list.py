#!/usr/bin/env python3


"""nまたはNから始まる英単語のリストを出力する
"""


def n_N_list_func():
    """nまたはNから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> n_N_list_func()
    n-list:
    <BLANKLINE>
        negative
    """

    print('n-list:')
    print('')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    n_N_en_words = sorted(['negative'])

    [print('    {}'.format(i)) for i in n_N_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n_N_list_func()
