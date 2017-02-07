#!/usr/bin/env python3


"""
"""

# i
#
# individual
from re_en.individual_re import individual_re_func
from print_ja.individual_ja import individual_ja_func

# individuality
from re_en.individuality_re import individuality_re_func
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
