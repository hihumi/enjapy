#!/usr/bin/env python3


"""main.pyで入力されたwordが、
axxx_reモジュールのaxxx_re_func()で作成した正規表現のa、またはAからはじまる英単語と合致した場合、
axxx_jaモジュールのaxxx_ja_func()を呼ぶ
ただし、a-listまたはA-list(すべて大文字小文字は問わない)と入力された場合、a_A_listモジュールのa_A_list_func()を呼ぶ
"""


# a: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# axxx:
# from re_en.axxx_re import axxx_re_func
#
# a:
from re_en.a_re import a_re_func
# area:
from re_en.area_re import area_re_func
# assure:
from re_en.assure_re import assure_re_func
# assurance:
from re_en.assurance_re import assurance_re_func
# attitude:
from re_en.attitude_re import attitude_re_func

# a-list:
from re_en.a_A_list_re import a_A_list_re_func


# a: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# axxx:
# from print_ja.axxx_ja import axxx_ja_func
# a:
from print_ja.a_ja import a_ja_func
# area:
from print_ja.area_ja import area_ja_func
# assure:
from print_ja.assure_ja import assure_ja_func
# assurance:
from print_ja.assurance_ja import assurance_ja_func
# attitude:
from print_ja.attitude_ja import attitude_ja_func


# a-list:
from print_en_lists.a_A_list import a_A_list_func


def a_A_re_search_en_func(a_A_word):
    """main.pyで入力されたwordが、
    axxx_reモジュールのaxxx_re_func()で作成した正規表現のa、またはAからはじまる英単語と合致した場合、
    axxx_jaモジュールのaxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、a_A_listモジュールのa_A_list_func()を呼ぶ
    """

    # a: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if a_re_func().search(a_A_word): # a
        a_ja_func()
    elif area_re_func().search(a_A_word): # area
        area_ja_func()
    elif assure_re_func().search(a_A_word): # assure
        assure_ja_func()
    elif assurance_re_func().search(a_A_word): # assurance
        assurance_ja_func()
    elif attitude_re_func().search(a_A_word): # attitude
        attitude_ja_func()
    elif a_A_list_re_func().search(a_A_word): # a-list
        a_A_list_func()
    else:
        print('not found...')

if __name__ == '__main__':
    word2 = 'python3'
    a_A_re_search_en_func(word2)
