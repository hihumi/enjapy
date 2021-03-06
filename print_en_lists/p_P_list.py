#!/usr/bin/env python3


"""pまたはPから始まる英単語のリストを出力する
"""


def p_P_list_func():
    """pまたはPから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> p_P_list_func()
    p-list:
    <BLANKLINE>
        part
        pay
        plan
        positive
        price
        problem
        product
    """

    print('p-list:')
    print('')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    p_P_en_words = sorted(['pay', 'positive', 'price', 'problem', 'part', 'plan', 'product'])

    [print('    {}'.format(i)) for i in p_P_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    p_P_list_func()
