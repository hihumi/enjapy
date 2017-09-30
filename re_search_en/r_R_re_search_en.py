#!/usr/bin/env python3


"""main.pyで入力されたwordが、
rxxx_reモジュールのrxxx_re_func()で作成した正規表現のr、またはRからはじまる英単語と合致した場合、
rxxx_jaモジュールのrxxx_ja_func()を呼ぶ
ただし、r-listまたはR-list(すべて大文字小文字は問わない)と入力された場合、r_R_listモジュールのr_R_list_func()を呼ぶ
"""


# r: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# rxxx:
# from re_en.rxxx_re import rxxx_re_func
#
# rate:
from re_en.rate_re import rate_re_func
# receive:
from re_en.receive_re import receive_re_func
# report:
from re_en.report_re import report_re_func
# respect:
from re_en.respect_re import respect_re_func
# respectable:
from re_en.respectable_re import respectable_re_func
# respectful:
from re_en.respectful_re import respectful_re_func
# room:
from re_en.room_re import room_re_func

# r-list:
from re_en.r_R_list_re import r_R_list_re_func


# r: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# rxxx:
# from print_ja.rxxx_ja import rxxx_ja_func
# rate:
from print_ja.rate_ja import rate_ja_func
# receive
from print_ja.receive_ja import receive_ja_func
# report:
from print_ja.report_ja import report_ja_func
# respect:
from print_ja.respect_ja import respect_ja_func
# respectable:
from print_ja.respectable_ja import respectable_ja_func
# respectful:
from print_ja.respectful_ja import respectful_ja_func
# room:
from print_ja.room_ja import room_ja_func


# r-list:
from print_en_lists.r_R_list import r_R_list_func


def r_R_re_search_en_func(r_R_word):
    """main.pyで入力されたwordが、
    rxxx_reモジュールのrxxx_re_func()で作成した正規表現のr、またはRからはじまる英単語と合致した場合、
    rxxx_jaモジュールのrxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、r_R_listモジュールのr_R_list_func()を呼ぶ
    """

    # r: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if rate_re_func().search(r_R_word): # rate
        rate_ja_func()
    elif receive_re_func().search(r_R_word): # receive
        receive_ja_func()
    elif report_re_func().search(r_R_word): # report
        report_ja_func()
    elif respect_re_func().search(r_R_word): # respect
        respect_ja_func()
    elif respectable_re_func().search(r_R_word): # respectable
        respectable_ja_func()
    elif respectful_re_func().search(r_R_word): # respectful
        respectful_ja_func()
    elif room_re_func().search(r_R_word): # room
        room_ja_func()
    elif r_R_list_re_func().search(r_R_word): # r-list
        r_R_list_func()
    else:
        print('not found...')
