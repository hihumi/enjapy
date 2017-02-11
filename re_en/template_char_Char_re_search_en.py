#!/usr/bin/env python3


"""main.pyで入力されたwordが、
charxxx_reモジュールのcharxxx_re_func()で作成した正規表現のchar、またはCharからはじまる英単語と合致した場合、
charxxx_jaモジュールのcharxxx_ja_func()を呼ぶ
"""


# char: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.charxxx_re import charxxx_re_func
# xxx:
from re_en.xxx_re import xxx_re_func

# char: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.charxxx_ja import charxxx_ja_func
# xxx:
from print_ja.xxx_ja import xxx_ja_func


def char_Char_re_search_en_func(word):
    """main.pyで入力されたwordが、
    charxxx_reモジュールのcharxxx_re_func()で作成した正規表現のchar、またはCharからはじまる英単語と合致した場合、
    charxxx_jaモジュールのcharxxx_ja_func()を呼ぶ関数
    """

    # char
    if xxx_re_func().search(word): # xxx
        xxx_ja_func()
    elif yyy_re_func().search(word): # yyy
        yyy_ja_func()
    #elif :
    else:
        print('not found...')
