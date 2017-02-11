#!/usr/bin/env python3


"""main.pyで入力されたwordが、
oxxx_reモジュールのoxxx_re_func()で作成した正規表現のo、またはOからはじまる英単語と合致した場合、
oxxx_jaモジュールのoxxx_ja_func()を呼ぶ
"""


# o
#
# from re_en.oxxx_re import oxxx_re_func
# outlook:
from re_en.outlook_re import outlook_re_func

# from print_ja.oxxx_ja import oxxx_ja_func
# outlook:
from print_ja.outlook_ja import outlook_ja_func


def o_O_re_search_en_func(word):
    """main.pyで入力されたwordが、
    oxxx_reモジュールのoxxx_re_func()で作成した正規表現のo、またはOからはじまる英単語と合致した場合、
    oxxx_jaモジュールのoxxx_ja_func()を呼ぶ関数
    """

    # o
    if outlook_re_func().search(word): # outlook:
        outlook_ja_func()
    # elif yyy_re_func().search(word): # yyy
    #    yyy_ja_func()
    #elif :
    else:
        print('not found...')
