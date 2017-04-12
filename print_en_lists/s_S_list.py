#!/usr/bin/env python3


"""sまたはSから始まる英単語のリストを出力する
"""


def s_S_list_func():
    """sまたはSから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> s_S_list_func()
    s-list:
    <BLANKLINE>
        sale
        service
        store
    """

    print('s-list:')
    print()

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    s_S_en_words = sorted(['service', 'store', 'sale'])

    [print('    {}'.format(i)) for i in s_S_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    s_S_list_func()
