#!/usr/bin/env python3


"""main.pyで入力されたwordが、
nxxx_reモジュールのnxxx_re_func()で作成した正規表現のn、またはNからはじまる英単語と合致した場合、
nxxx_jaモジュールのnxxx_ja_func()を呼ぶ
"""


# n: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.nxxx_re import nxxx_re_func
# negative:
from re_en.negative_re import negative_re_func

# from print_ja.nxxx_ja import nxxx_ja_func
# negative:
from print_ja.negative_ja import negative_ja_func


def n_N_re_search_en_func(n_N_word):
    """main.pyで入力されたwordが、
    nxxx_reモジュールのnxxx_re_func()で作成した正規表現のn、またはNからはじまる英単語と合致した場合、
    nxxx_jaモジュールのnxxx_ja_func()を呼ぶ関数
    """

    # n: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if negative_re_func().search(n_N_word): # negative
        negative_ja_func()
    # elif yyy_re_func().search(word): # yyy
    #    yyy_ja_func()
    else:
        print('not found...')
