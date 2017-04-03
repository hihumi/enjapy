#!/usr/bin/env python3


"""main.pyで入力されたwordが、
pxxx_reモジュールのpxxx_re_func()で作成した正規表現のp、またはPからはじまる英単語と合致した場合、
pxxx_jaモジュールのpxxx_ja_func()を呼ぶ
"""


# p: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.pxxx_re import pxxx_re_func
# pay:
from re_en.pay_re import pay_re_func
# positive:
from re_en.positive_re import positive_re_func


# p: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.pxxx_ja import pxxx_ja_func
# pay:
from print_ja.pay_ja import pay_ja_func
# positive:
from print_ja.positive_ja import positive_ja_func



def p_P_re_search_en_func(p_P_word):
    """main.pyで入力されたwordが、
    pxxx_reモジュールのpxxx_re_func()で作成した正規表現のp、またはpからはじまる英単語と合致した場合、
    pxxx_jaモジュールのpxxx_ja_func()を呼ぶ関数
    """

    # p: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if pay_re_func().search(p_P_word):
        pay_ja_func()
    elif positive_re_func().search(p_P_word): # positive
        positive_ja_func()
    else:
        print('not found...')
