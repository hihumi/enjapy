#!/usr/bin/env python3


"""charまたはCharから始まる英単語のリストを出力する
"""


def char_Char_list_func():
    """charまたはcharから始まる英単語のリストをソートし出力する関数

    doctest:
    >>> char_Char_list_func()
    (テスト対象の英単語)
    """

    char_Char_en_words = sorted(['assure', 'assurance'])

    [print(i) for i in char_Char_en_words]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    char_Char_list_func()
