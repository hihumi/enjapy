#!/usr/bin/env python3


"""aまたはAから始まる英単語のリストを出力する
"""


def a_A_list_func():
    """aまたはAから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> a_A_list_func()
    a-list:
    assurance
    assure
    """

    print('a-list:')

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    a_A_en_words = sorted(['assure', 'assurance'])

    [print(i) for i in a_A_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    a_A_list_func()
