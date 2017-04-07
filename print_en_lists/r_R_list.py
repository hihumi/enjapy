#!/usr/bin/env python3


"""rまたはRから始まる英単語のリストを出力する
"""


def r_R_list_func():
    """rまたはRから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> r_R_list_func()
    r-list:
        rate
        respect
        respectable
        respectful
    """

    print('r-list:')

    r_R_en_words = sorted(['respect', 'respectable', 'respectful', 'rate'])

    [print('    {}'.format(i)) for i in r_R_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    r_R_list_func()
