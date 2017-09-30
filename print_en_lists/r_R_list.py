#!/usr/bin/env python3


"""rまたはRから始まる英単語のリストを出力する
"""


def r_R_list_func():
    """rまたはRから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> r_R_list_func()
    r-list:
    <BLANKLINE>
        rate
        receive
        report
        respect
        respectable
        respectful
        room
    """

    print('r-list:')
    print('')

    r_R_en_words = sorted(['respect', 'respectable', 'respectful', 'report', 'rate',
                           'room', 'receive'])

    [print('    {}'.format(i)) for i in r_R_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    r_R_list_func()
