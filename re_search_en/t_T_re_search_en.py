#!/usr/bin/env python3


"""main.pyで入力されたwordが、
txxx_reモジュールのtxxx_re_func()で作成した正規表現のt、またはTからはじまる英単語と合致した場合、
txxx_jaモジュールのtxxx_ja_func()を呼ぶ
ただし、t-listまたはt-list(すべて大文字小文字は問わない)と入力された場合、t_T_listモジュールのt_T_list_func()を呼ぶ
"""


# t: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.txxx_re import txxx_re_func
# tax:
from re_en.tax_re import tax_re_func

# t-list:
from re_en.t_T_list_re import t_T_list_re_func


# t: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.txxx_ja import txxx_ja_func
# tax:
from print_ja.tax_ja import tax_ja_func


# t-list:
from print_en_lists.t_T_list import t_T_list_func


def t_T_re_search_en_func(t_T_word):
    """main.pyで入力されたwordが、
    txxx_reモジュールのtxxx_re_func()で作成した正規表現のt、またはtからはじまる英単語と合致した場合、
    txxx_jaモジュールのtxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、t_T_listモジュールのt_T_list_func()を呼ぶ
    """

    # t: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if tax_re_func().search(t_T_word): # tax
        tax_ja_func()
    elif t_T_list_re_func().search(t_T_word): # t-list
        t_T_list_func()
    else:
        print('not found...')
