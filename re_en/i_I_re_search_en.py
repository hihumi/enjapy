#!/usr/bin/env python3


"""
"""


# a b c d e f g h i j k l m n o p q r s t u v w x y z
# i
#
# from re_en.i_re import i_re_func
# individual
from re_en.individual_re import individual_re_func
# individuality
from re_en.individuality_re import individuality_re_func

# from print_ja.i_ja import i_ja_func
# individual
from print_ja.individual_ja import individual_ja_func
# individuality
from print_ja.individuality_ja import individuality_ja_func

def i_I_re_search_en_func(word):
    """
    """

    # i
    if individual_re_func().search(word): # individual
        individual_ja_func()
    elif individuality_re_func().search(word): # individuality
        individuality_ja_func()
    else:
        print('not found...')
