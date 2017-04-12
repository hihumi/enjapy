#!/usr/bin/env python3


"""jまたはJから始まる英単語のリストを出力する
"""


def j_J_list_func():
    """uまたはuから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> j_J_list_func()
    j-list:
    <BLANKLINE>
        job
    """

    print('j-list:')
    print()

    # アルファベット順にソートされるので、リスト(配列)末尾に英単語を追加してくだけでいい
    j_J_en_words = sorted(['job'])

    [print('    {}'.format(i)) for i in j_J_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    j_J_list_func()
