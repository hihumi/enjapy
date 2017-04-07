#!/usr/bin/env python3


"""main.pyで入力されたwordが、
jxxx_reモジュールのjxxx_re_func()で作成した正規表現のj、またはJからはじまる英単語と合致した場合、
jxxx_jaモジュールのjxxx_ja_func()を呼ぶ
ただし、j-listまたはJ-list(すべて大文字小文字は問わない)と入力された場合、j_J_listモジュールのj_J_list_func()を呼ぶ
"""


# j: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.jxxx_re import jxxx_re_func
# job:
from re_en.job_re import job_re_func

# j-list:
from re_en.j_J_list_re import j_J_list_re_func


# j: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.jxxx_ja import jxxx_ja_func
# job:
from print_ja.job_ja import job_ja_func


# j-list:
from print_en_lists.j_J_list import j_J_list_func


def j_J_re_search_en_func(j_J_word):
    """main.pyで入力されたwordが、
    jxxx_reモジュールのjxxx_re_func()で作成した正規表現のj、またはJからはじまる英単語と合致した場合、
    jxxx_jaモジュールのjxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、j_J_listモジュールのj_J_list_func()を呼ぶ
    """

    # j: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if job_re_func().search(j_J_word): # job
        job_ja_func()
    elif j_J_list_re_func().search(j_J_word): # j-list
        j_J_list_func()
    else:
        print('not found...')
