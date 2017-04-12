#!/usr/bin/env python3


"""wまたはWから始まる英単語のリストを出力する
"""


def w_W_list_func():
    """wまたはwから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> w_W_list_func()
    w-list:
    <BLANKLINE>
        want
        way
        will
        willpower
    """

    print('w-list:')
    print()

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    w_W_en_words = sorted(['want', 'way', 'will', 'willpower'])

    [print('    {}'.format(i)) for i in w_W_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    w_W_list_func()
