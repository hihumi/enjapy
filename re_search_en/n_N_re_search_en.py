#!/usr/bin/env python3


"""main.pyで入力されたwordが、
nxxx_reモジュールのnxxx_re_func()で作成した正規表現のn、またはNからはじまる英単語と合致した場合、
nxxx_jaモジュールのnxxx_ja_func()を呼ぶ
ただし、n-listまたはN-list(すべて大文字小文字は問わない)と入力された場合、n_N_listモジュールのn_N_list_func()を呼ぶ
"""


# n: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.nxxx_re import nxxx_re_func
# negative:
from re_en.negative_re import negative_re_func

# n-list:
from re_en.n_N_list_re import n_N_list_re_func

# from print_ja.nxxx_ja import nxxx_ja_func
# negative:
from print_ja.negative_ja import negative_ja_func


# n-list:
from print_en_lists.n_N_list import n_N_list_func


def n_N_re_search_en_func(n_N_word):
    """main.pyで入力されたwordが、
    nxxx_reモジュールのnxxx_re_func()で作成した正規表現のn、またはNからはじまる英単語と合致した場合、
    nxxx_jaモジュールのnxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、n_N_listモジュールのn_N_list_func()を呼ぶ
    """

    # n: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if negative_re_func().search(n_N_word): # negative
        negative_ja_func()
    elif n_N_list_re_func().search(n_N_word): # n-list
        n_N_list_func()
    else:
        print('not found...')
