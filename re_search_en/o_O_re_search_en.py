#!/usr/bin/env python3


"""main.pyで入力されたwordが、
oxxx_reモジュールのoxxx_re_func()で作成した正規表現のo、またはOからはじまる英単語と合致した場合、
oxxx_jaモジュールのoxxx_ja_func()を呼ぶ
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

# o: a b c d e f g h i j k l m n o p q r s t u v w x y z

# from print_ja.oxxx_ja import oxxx_ja_func
# office:
from print_ja.office_ja import office_ja_func
# order:
from print_ja.order_ja import order_ja_func
# outlook:
from print_ja.outlook_ja import outlook_ja_func


def o_O_re_search_en_func(word):
    """main.pyで入力されたwordが、
    oxxx_reモジュールのoxxx_re_func()で作成した正規表現のo、またはOからはじまる英単語と合致した場合、
    oxxx_jaモジュールのoxxx_ja_func()を呼ぶ関数
    """

    # o: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if office_re_func().search(word): # office
        office_ja_func()
    elif order_re_func().search(word):
        order_ja_func()
    elif outlook_re_func().search(word): # outlook
        outlook_ja_func()
    # elif yyy_re_func().search(word): # yyy
    #    yyy_ja_func()
    else:
        print('not found...')
