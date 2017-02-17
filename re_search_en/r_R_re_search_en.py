#!/usr/bin/env python3


"""main.pyで入力されたwordが、
rxxx_reモジュールのrxxx_re_func()で作成した正規表現のr、またはRからはじまる英単語と合致した場合、
rxxx_jaモジュールのrxxx_ja_func()を呼ぶ
"""

# r: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.r_re import r_re_func
# respect:
from re_en.respect_re import respect_re_func
# respectable:
from re_en.respectable_re import respectable_re_func
# respectful:
from re_en.respectful_re import respectful_re_func

# r: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.r_ja import r_ja_func
# respect:
from print_ja.respect_ja import respect_ja_func
# respectable:
from print_ja.respectable_ja import respectable_ja_func
# respectful:
from print_ja.respectful_ja import respectful_ja_func


def r_R_re_search_en_func(word):
    """main.pyで入力されたwordが、
    rxxx_reモジュールのrxxx_re_func()で作成した正規表現のr、またはRからはじまる英単語と合致した場合、
    rxxx_jaモジュールのrxxx_ja_func()を呼ぶ関数
    """

    # r
    if respect_re_func().search(word): # respect
        respect_ja_func()
    elif respectable_re_func().search(word): # respectable
        respectable_ja_func()
    elif respectful_re_func().search(word): # respectful
        respectful_ja_func()
    else:
        print('not found...')
