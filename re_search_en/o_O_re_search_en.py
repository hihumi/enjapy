#!/usr/bin/env python3


"""main.pyで入力されたwordが、
oxxx_reモジュールのoxxx_re_func()で作成した正規表現のo、またはOからはじまる英単語と合致した場合、
oxxx_jaモジュールのoxxx_ja_func()を呼ぶ
ただし、o-listまたはO-list(すべて大文字小文字は問わない)と入力された場合、o_O_listモジュールのo_O_list_func()を呼ぶ
"""


# o: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.oxxx_re import oxxx_re_func
# office:
from re_en.office_re import office_re_func
# order:
from re_en.order_re import order_re_func
# outlook:
from re_en.outlook_re import outlook_re_func

# 0-list:
from re_en.o_O_list_re import o_O_list_re_func


# o: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.oxxx_ja import oxxx_ja_func
# office:
from print_ja.office_ja import office_ja_func
# order:
from print_ja.order_ja import order_ja_func
# outlook:
from print_ja.outlook_ja import outlook_ja_func


from print_en_lists.o_O_list import o_O_list_func


def o_O_re_search_en_func(o_O_word):
    """main.pyで入力されたwordが、
    oxxx_reモジュールのoxxx_re_func()で作成した正規表現のo、またはOからはじまる英単語と合致した場合、
    oxxx_jaモジュールのoxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、o_O_listモジュールのo_O_list_func()を呼ぶ
    """

    # o: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if office_re_func().search(o_O_word): # office
        office_ja_func()
    elif order_re_func().search(o_O_word): # order
        order_ja_func()
    elif outlook_re_func().search(o_O_word): # outlook
        outlook_ja_func()
    elif o_O_list_re_func().search(o_O_word): # o-list
        o_O_list_func()
    else:
        print('not found...')
