#!/usr/bin/env python3


"""main.pyで入力されたwordが、
nxxx_reモジュールのnxxx_re_func()で作成した正規表現のn、またはNからはじまる英単語と合致した場合、
nxxx_jaモジュールのnxxx_ja_func()を呼ぶ
"""


# n: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.xxx_re import xxx_re_func
# negative:
from re_en.negative_re import negative_re_func

# from print_ja.xxx_ja import xxx_ja_func
# negative:
from print_ja.negative_ja import negative_ja_func


def n_N_re_search_en_func(word):
    """main.pyで入力されたwordが、
    nxxx_reモジュールのnxxx_re_func()で作成した正規表現のn、またはNからはじまる英単語と合致した場合、
    nxxx_jaモジュールのnxxx_ja_func()を呼ぶ関数
    """

    # n
    if negative_re_func().search(word): # negative:
        negative_ja_func()
    # elif yyy_re_func().search(word): # yyy
    #    yyy_ja_func()
    #elif :
    else:
        print('not found...')
