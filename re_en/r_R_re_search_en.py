#!/usr/bin/env python3


"""
"""


# r
#
# from re_en.r_re import r_re_func
# respect
from re_en.respect_re import respect_re_func
# respectable
from re_en.respectable_re import respectable_re_func
# respectful
from re_en.respectful_re import respectful_re_func

# from print_ja.r_ja import r_ja_func
# respect
from print_ja.respect_ja import respect_ja_func
# respectable
from print_ja.respectable_ja import respectable_ja_func
# respectful
from print_ja.respectful_ja import respectful_ja_func


def r_R_re_search_en_func(word):
    """
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
