#!/usr/bin/env python3


"""main.pyで入力されたwordが、
sxxx_reモジュールのsxxx_re_func()で作成した正規表現のs、またはSからはじまる英単語と合致した場合、
sxxx_jaモジュールのsxxx_ja_func()を呼ぶ
"""


# s: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.sxxx_re import sxxx_re_func
# service:
from re_en.service_re import service_re_func
# store:
from re_en.store_re import store_re_func


# s: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.sxxx_ja import sxxx_ja_func
# service:
from print_ja.service_ja import service_ja_func
from print_ja.store_ja import store_ja_func


def s_S_re_search_en_func(s_S_word):
    """main.pyで入力されたwordが、
    sxxx_reモジュールのsxxx_re_func()で作成した正規表現のs、またはsからはじまる英単語と合致した場合、
    sxxx_jaモジュールのsxxx_ja_func()を呼ぶ関数
    """

    # s: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if service_re_func().search(s_S_word): # service
        service_ja_func()
    elif store_re_func().search(s_S_word): # store
        store_ja_func()
    else:
        print('not found...')
