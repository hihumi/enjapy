#!/usr/bin/env python3


"""main.pyで入力されたwordが、
cxxx_reモジュールのcxxx_re_func()で作成した正規表現のc、またはCからはじまる英単語と合致した場合、
cxxx_jaモジュールのcxxx_ja_func()を呼ぶ
"""


# c: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.cxxx_re import cxxx_re_func
# company:
from re_en.company_re import company_re_func


# c: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.cxxx_ja import cxxx_ja_func
# company:
from print_ja.company_ja import company_ja_func


def c_C_re_search_en_func(word):
    """main.pyで入力されたwordが、
    cxxx_reモジュールのcxxx_re_func()で作成した正規表現のc、またはcからはじまる英単語と合致した場合、
    cxxx_jaモジュールのcxxx_ja_func()を呼ぶ関数
    """

    # c: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if company_re_func().search(word): # xxx
        company_ja_func()
    #elif yyy_re_func().search(word): # yyy
    #    yyy_ja_func()
    else:
        print('not found...')
