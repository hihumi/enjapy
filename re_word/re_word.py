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

    man_re = re.compile(r'man$', re.I)
    you_re = re.compile(r'you$', re.I)

    if man_re.search(word):
        man.man()
    elif you_re.search(word):
        you.you()
    else:
        print('not found...')
