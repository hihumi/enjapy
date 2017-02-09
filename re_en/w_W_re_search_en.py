#!/usr/bin/env python3


"""
"""

# w
#
# from re_en.w_re import w_re_func
# will
from re_en.will_re import will_re_func
# willpower
from re_en.willpower_re import willpower_re_func

# from print_ja.w_ja import w_ja_func
# will
from print_ja.will_ja import will_ja_func
# willpower
from print_ja.willpower_ja import willpower_ja_func


def w_W_re_search_en_func(word):
    """
    """

    # w
    if will_re_func().search(word): # will
        will_ja_func()
    elif willpower_re_func().search(word): # willpower
        willpower_ja_func()
    else:
        print('not found...')
