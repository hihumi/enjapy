#!/usr/bin/env python3


"""main.pyで入力されたwordが、
mxxx_reモジュールのmxxx_re_func()で作成した正規表現のm、またはMからはじまる英単語と合致した場合、
mxxx_jaモジュールのmxxx_ja_func()を呼ぶ
"""


# m: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.mxxx_re import mxxx_re_func
# maintain:
from re_en.maintain_re import maintain_re_func

# m: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.nxxx_ja import nxxx_ja_func
# maintain:
from print_ja.maintain_ja import maintain_ja_func


def m_M_re_search_en_func(word):
    """main.pyで入力されたwordが、
    mxxx_reモジュールのmxxx_re_func()で作成した正規表現のm、またはMからはじまる英単語と合致した場合、
    mxxx_jaモジュールのmxxx_ja_func()を呼ぶ関数
    """

    # m:
    if maintain_re_func().search(word): # maintain
        maintain_ja_func()
    # elif yyy_re_func().search(word): # yyy
    #     yyy_ja_func()
    #elif :
    else:
        print('not found...')
