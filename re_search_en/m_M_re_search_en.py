#!/usr/bin/env python3


"""main.pyで入力されたwordが、
mxxx_reモジュールのmxxx_re_func()で作成した正規表現のm、またはMからはじまる英単語と合致した場合、
mxxx_jaモジュールのmxxx_ja_func()を呼ぶ
ただし、m-listまたはM-list(すべて大文字小文字は問わない)と入力された場合、m_M_listモジュールのm_M_list_func()を呼ぶ
"""


# m: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.mxxx_re import mxxx_re_func
# maintain:
from re_en.maintain_re import maintain_re_func
# market
from re_en.market_re import market_re_func

# m-list:
from re_en.m_M_list_re import m_M_list_re_func


# m: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja.mxxx_ja import mxxx_ja_func
# maintain:
from print_ja.maintain_ja import maintain_ja_func
# market
from print_ja.market_ja import market_ja_func


# m-list:
from print_en_lists.m_M_list import m_M_list_func


def m_M_re_search_en_func(m_M_word):
    """main.pyで入力されたwordが、
    mxxx_reモジュールのmxxx_re_func()で作成した正規表現のm、またはMからはじまる英単語と合致した場合、
    mxxx_jaモジュールのmxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、m_M_listモジュールのm_M_list_func()を呼ぶ
    """

    # m: a b c d e f g h i j k l m n o p q r s t u v w x y z
    if maintain_re_func().search(m_M_word): # maintain
        maintain_ja_func()
    elif market_re_func().search(m_M_word): # market
         market_ja_func()
    elif m_M_list_re_func().search(m_M_word): # m-list
        m_M_list_func()
    else:
        print('not found...')
