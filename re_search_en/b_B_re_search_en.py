#!/usr/bin/env python3


"""main.pyで入力されたwordが、
bxxx_reモジュールのbxxx_re_func()で作成した正規表現のb、またはBからはじまる英単語と合致した場合、
bxxx_jaモジュールのbxxx_ja_func()を呼ぶ
"""


# b: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.bxxx_re import bxxx_re_func
# business:
from re_en.business_re import business_re_func

# b: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.bxxx_ja import bxxx_ja_func
# business:
from print_ja.business_ja import business_ja_func


def b_B_re_search_en_func(b_B_word):
    """main.pyで入力されたwordが、
    bxxx_reモジュールのbxxx_re_func()で作成した正規表現のb、またはBからはじまる英単語と合致した場合、
    bxxx_jaモジュールのbxxx_ja_func()を呼ぶ関数
    """

    # b: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if business_re_func().search(b_B_word): # business
        business_ja_func()
    #elif yyy_re_func().search(b_B_word): # yyy
    #    yyy_ja_func()
    #elif :
    else:
        print('not found...')
