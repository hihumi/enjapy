#!/usr/bin/env python3


"""main.pyで入力されたwordが、
wxxx_reモジュールのwxxx_re_func()で作成した正規表現のw、またはWからはじまる英単語と合致した場合、
wxxx_jaモジュールのwxxx_ja_func()を呼ぶ
"""


# w: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.w_re import w_re_func
# will:
from re_en.will_re import will_re_func
# willpower:
from re_en.willpower_re import willpower_re_func

# w: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.w_ja import w_ja_func
# will:
from print_ja.will_ja import will_ja_func
# willpower:
from print_ja.willpower_ja import willpower_ja_func


def w_W_re_search_en_func(word):
    """main.pyで入力されたwordが、
    wxxx_reモジュールのwxxx_re_func()で作成した正規表現のw、またはWからはじまる英単語と合致した場合、
    wxxx_jaモジュールのwxxx_ja_func()を呼ぶ関数
    """

    # w:
    if will_re_func().search(word): # will
        will_ja_func()
    elif willpower_re_func().search(word): # willpower
        willpower_ja_func()
    else:
        print('not found...')
