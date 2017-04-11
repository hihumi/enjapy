#!/usr/bin/env python3


"""main.pyで入力されたwordが、
fxxx_reモジュールのfxxx_re_func()で作成した正規表現のf、またはFからはじまる英単語と合致した場合、
fxxx_jaモジュールのfxxx_ja_func()を呼ぶ
ただし、f-listまたはF-list(すべて大文字小文字は問わない)と入力された場合、f_F_listモジュールのf_F_list_func()を呼ぶ
"""


# f: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# fxxx:
# from re_en.fxxx_re import fxxx_re_func
#
# free:
from re_en.free_re import free_re_func

# f-list:
from re_en.f_F_list_re import f_F_list_re_func


# f: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# fxxx:
# from print_ja.fxxx_ja import fxxx_ja_func
#
# free:
from print_ja.free_ja import free_ja_func


# f-list:
from print_en_lists.f_F_list import f_F_list_func


def f_F_re_search_en_func(f_F_word):
    """main.pyで入力されたwordが、
    fxxx_reモジュールのfxxx_re_func()で作成した正規表現のf、またはFからはじまる英単語と合致した場合、
    fxxx_jaモジュールのfxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、f_F_listモジュールのf_F_list_func()を呼ぶ
    """

    # f: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if free_re_func().search(f_F_word): # free
        free_ja_func()
    elif f_F_list_re_func().search(f_F_word): # f-list
         f_F_list_func()
    else:
        print('not found...')
