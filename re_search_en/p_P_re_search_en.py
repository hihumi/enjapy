#!/usr/bin/env python3


"""main.pyで入力されたwordが、
pxxx_reモジュールのpxxx_re_func()で作成した正規表現のp、またはPからはじまる英単語と合致した場合、
pxxx_jaモジュールのpxxx_ja_func()を呼ぶ
ただし、p-listまたはP-list(すべて大文字小文字は問わない)と入力された場合、p_P_listモジュールのp_P_list_func()を呼ぶ
"""


# p: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.pxxx_re import pxxx_re_func
# pxxx:
#
# part:
from re_en.part_re import part_re_func
# pay:
from re_en.pay_re import pay_re_func
# plan:
from re_en.plan_re import plan_re_func
# positive:
from re_en.positive_re import positive_re_func
# price:
from re_en.price_re import price_re_func
# problem
from re_en.problem_re import problem_re_func
# product:
from re_en.product_re import product_re_func


# p-list:
from re_en.p_P_list_re import p_P_list_re_func


# p: a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# pxxx:
# from print_ja.pxxx_ja import pxxx_ja_func
#
# part:
from print_ja.part_ja import part_ja_func
# pay:
from print_ja.pay_ja import pay_ja_func
# plan:
from print_ja.plan_ja import plan_ja_func
# positive:
from print_ja.positive_ja import positive_ja_func
# price:
from print_ja.price_ja import price_ja_func
# problem
from print_ja.problem_ja import problem_ja_func
# product:
from print_ja.product_ja import product_ja_func



from print_en_lists.p_P_list import p_P_list_func


def p_P_re_search_en_func(p_P_word):
    """main.pyで入力されたwordが、
    pxxx_reモジュールのpxxx_re_func()で作成した正規表現のp、またはpからはじまる英単語と合致した場合、
    pxxx_jaモジュールのpxxx_ja_func()を呼ぶ関数
    ただし、最後のelifは、p_P_listモジュールのp_P_list_func()を呼ぶ
    """

    # p: a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # elif pxxx_re_func().search(p_P_word): # pxxx
    #     pxxx_ja_func()
    #
    if part_re_func().search(p_P_word): # part
        part_ja_func()
    elif pay_re_func().search(p_P_word): # pay
        pay_ja_func()
    elif plan_re_func().search(p_P_word): # plan
        plan_ja_func()
    elif positive_re_func().search(p_P_word): # positive
        positive_ja_func()
    elif price_re_func().search(p_P_word): # price
        price_ja_func()
    elif problem_re_func().search(p_P_word): # problem
        problem_ja_func()
    elif product_re_func().search(p_P_word): # product
        product_ja_func()
    elif p_P_list_re_func().search(p_P_word): # p-list
        p_P_list_func()
    else:
        print('not found...')
