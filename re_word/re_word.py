#!/usr/bin/env python3


"""このスクリプトは、main.pyで入力されたwordの正規表現をチェックする。
"""


import re

from print_word import you
from print_word import man


def re_word(word):
    """この関数は、main.pyで入力されたwordが、正規表現に合致するかどうか調べ、
    dir: print_wordにある各関数を呼び出す。
    """

    man_re = re.compile(r'[mM]an')
    you_re = re.compile(r'[yY]ou')

    if man_re.match(word): # or searcn()
        man.man()
    elif you_re.match(word):
        you.you()
    else:
        print('not found...')

if __name__ == '__main__':
    outer_word = 'enjapy'
    re_word(outer_word)
