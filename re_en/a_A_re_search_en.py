#!/usr/bin/env python3


"""main.pyで入力されたwordが、
axxx_reモジュールのaxxx_re_func()で作成した正規表現のa、またはAからはじまる英単語と合致した場合、
axxx_jaモジュールのaxxx_ja_func()を呼ぶ
"""


# a: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.xxx_re import xxx_re_func
# a:
from re_en.a_re import a_re_func
# assure:
from re_en.assure_re import assure_re_func
# assurance:
from re_en.assurance_re import assurance_re_func

# a: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# a:
from print_ja.a_ja import a_ja_func
# assure:
from print_ja.assure_ja import assure_ja_func
# assurance:
from print_ja.assurance_ja import assurance_ja_func


def a_A_re_search_en_func(word):
    """main.pyで入力されたwordが、
    axxx_reモジュールのaxxx_re_func()で作成した正規表現のa、またはAからはじまる英単語と合致した場合、
    axxx_jaモジュールのaxxx_ja_func()を呼ぶ関数
    """

    # a:
    if a_re_func().search(word): # a:
        a_ja_func()
    elif assure_re_func().search(word): # assure:
        assure_ja_func()
    elif assurance_re_func().search(word): # assurance:
        assurance_ja_func()
    else:
        print('not found...')
