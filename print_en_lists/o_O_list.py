#!/usr/bin/env python3


"""o(オー)またはO(オー)から始まる英単語のリストを出力する
"""


def o_O_list_func():
    """oまたはOから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> o_O_list_func()
    o-list:
    <BLANKLINE>
        office
        order
        outlook
    """

    print('o-list:')
    print('')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    o_O_en_words = sorted(['office', 'order', 'outlook'])

    [print('    {}'.format(i)) for i in o_O_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    o_O_list_func()
