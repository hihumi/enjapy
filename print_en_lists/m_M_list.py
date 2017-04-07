#!/usr/bin/env python3


"""mまたはMから始まる英単語のリストを出力する
"""


def m_M_list_func():
    """mまたはMから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> m_M_list_func()
    m-list:
    maintain
    market
    """

    print('m-list:')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    m_M_en_words = sorted(['maintain', 'market'])

    [print(i) for i in m_M_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    m_M_list_func()
