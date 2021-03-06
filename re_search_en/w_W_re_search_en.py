#!/usr/bin/env python3


"""main.pyで入力されたwordが、
wxxx_reモジュールのwxxx_re_func()で作成した正規表現のw、またはWからはじまる英単語と合致した場合、
wxxx_jaモジュールのwxxx_ja_func()を呼ぶ
ただし、w-listまたはW-list(すべて大文字小文字は問わない)と入力された場合、w_W_listモジュールのw_W_list_func()を呼ぶ
"""


# w: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.wxxx_re import wxxx_re_func
# want
from re_en.want_re import want_re_func
# way:
from re_en.way_re import way_re_func
# will:
from re_en.will_re import will_re_func
# willpower:
from re_en.willpower_re import willpower_re_func

# w-list:
from re_en.w_W_list_re import w_W_list_re_func


# w: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.wxxx_ja import wxxx_ja_func
# want:
from print_ja.want_ja import want_ja_func
# way:
from print_ja.way_ja import way_ja_func
# will:
from print_ja.will_ja import will_ja_func
# willpower:
from print_ja.willpower_ja import willpower_ja_func


from print_en_lists.w_W_list import w_W_list_func


def w_W_re_search_en_func(w_W_word):
    """main.pyで入力されたwordが、
    wxxx_reモジュールのwxxx_re_func()で作成した正規表現のw、またはWからはじまる英単語と合致した場合、
    wxxx_jaモジュールのwxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、w_W_listモジュールのw_W_list_func()を呼ぶ
    """

    # w: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if want_re_func().search(w_W_word): # want
        want_ja_func()
    elif way_re_func().search(w_W_word): # way
        way_ja_func()
    elif will_re_func().search(w_W_word): # will
        will_ja_func()
    elif willpower_re_func().search(w_W_word): # willpower
        willpower_ja_func()
    elif w_W_list_re_func().search(w_W_word): # w-list
        w_W_list_func()
    else:
        print('not found...')
