#!/usr/bin/env python3


"""main.pyで入力されたwordが、
bxxx_reモジュールのbxxx_re_func()で作成した正規表現のb、またはBからはじまる英単語と合致した場合、
bxxx_jaモジュールのbxxx_ja_func()を呼ぶ
ただし、b-listまたはB-list(すべて大文字小文字は問わない)と入力された場合、b_B_listモジュールのb_B_list_func()を呼ぶ
"""


# b: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.bxxx_re import bxxx_re_func
# business:
from re_en.business_re import business_re_func
# base:
from re_en.base_re import base_re_func

# b-list:
from re_en.b_B_list_re import b_B_list_re_func


# b: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.bxxx_ja import bxxx_ja_func
# business:
from print_ja.business_ja import business_ja_func
# base:
from print_ja.base_ja import base_ja_func



# b-lsit:
from print_en_lists.b_B_list import b_B_list_func


def b_B_re_search_en_func(b_B_word):
    """main.pyで入力されたwordが、
    bxxx_reモジュールのbxxx_re_func()で作成した正規表現のb、またはBからはじまる英単語と合致した場合、
    bxxx_jaモジュールのbxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、b_B_listモジュールのb_B_list_func()を呼ぶ
    """

    # b: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if business_re_func().search(b_B_word): # business
        business_ja_func()
    elif base_re_func().search(b_B_word):
        base_ja_func()
    elif b_B_list_re_func().search(b_B_word): # b-list
        b_B_list_func()
    else:
        print('not found...')
