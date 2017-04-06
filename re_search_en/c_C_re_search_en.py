#!/usr/bin/env python3


"""main.pyで入力されたwordが、
cxxx_reモジュールのcxxx_re_func()で作成した正規表現のc、またはCからはじまる英単語と合致した場合、
cxxx_jaモジュールのcxxx_ja_func()を呼ぶ
ただし、c-listまたはC-list(すべて大文字小文字は問わない)と入力された場合、c_C_listモジュールのc_C_list_func()を呼ぶ
"""


# c: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.cxxx_re import cxxx_re_func
# call:
from re_en.call_re import call_re_func
# company:
from re_en.company_re import company_re_func

# c-list:
from re_en.c_C_list_re import c_C_list_re_func


# c: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.cxxx_ja import cxxx_ja_func
# call:
from print_ja.call_ja import call_ja_func
# company:
from print_ja.company_ja import company_ja_func


# c-list:
from print_en_lists.c_C_list import c_C_list_func


def c_C_re_search_en_func(c_C_word):
    """main.pyで入力されたwordが、
    cxxx_reモジュールのcxxx_re_func()で作成した正規表現のc、またはcからはじまる英単語と合致した場合、
    cxxx_jaモジュールのcxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、c_C_listモジュールのc_C_list_func()を呼ぶ
    """

    # c: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if call_re_func().search(c_C_word): # call
        call_ja_func()
    elif company_re_func().search(c_C_word): # company
        company_ja_func()
    elif c_C_list_re_func().search(c_C_word):
        c_C_list_func()
    else:
        print('not found...')
