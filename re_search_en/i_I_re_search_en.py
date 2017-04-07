#!/usr/bin/env python3


"""main.pyで入力されたwordが、
ixxx_reモジュールのixxx_re_func()で作成した正規表現のi、またはIからはじまる英単語と合致した場合、
ixxx_jaモジュールのixxx_ja_func()を呼ぶ
ただし、i-listまたはI-list(すべて大文字小文字は問わない)と入力された場合、i_I_listモジュールのi_I_list_func()を呼ぶ
"""


# i: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.i_re import i_re_func
# individual:
from re_en.individual_re import individual_re_func
# individuality:
from re_en.individuality_re import individuality_re_func

# i-list:
from re_en.i_I_list_re import i_I_list_re_func


# i: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.i_ja import i_ja_func
# individual:
from print_ja.individual_ja import individual_ja_func
# individuality:
from print_ja.individuality_ja import individuality_ja_func


# i-list:
from print_en_lists.i_I_list import i_I_list_func


def i_I_re_search_en_func(i_I_word):
    """main.pyで入力されたwordが、
    ixxx_reモジュールのixxx_re_func()で作成した正規表現のi、またはIからはじまる英単語と合致した場合、
    ixxx_jaモジュールのixxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、i_I_listモジュールのi_I_list_func()を呼ぶ
    """

    # i: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if individual_re_func().search(i_I_word): # individual
        individual_ja_func()
    elif individuality_re_func().search(i_I_word): # individuality
        individuality_ja_func()
    elif i_I_list_re_func().search(i_I_word): # i-list
        i_I_list_func()
    else:
        print('not found...')
