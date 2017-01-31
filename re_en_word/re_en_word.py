#!/usr/bin/env python3


"""このスクリプトは、main.pyで入力されたwordの正規表現をチェックする。
"""


import re

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# r
from print_ja_word import respect
from print_ja_word import respectful
from print_ja_word import respectable
# y
from print_ja_word import you
# m
from print_ja_word import man


def re_en_word(word):
    """この関数は、main.pyで入力されたwordが、正規表現に合致するかどうか調べ、
    dir: print_wordにある各関数を呼び出す。
    """

    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # a
    # b
    # c
    # d
    # e
    # f
    # g
    # h
    # i
    # j
    # k
    # l

    # m
    man_re = re.compile(r'man$', re.I)

    # n
    # o
    # p
    # q

    # r
    respect_re = re.compile(r'respect$', re.I)
    respectful_re = re.compile(r'respectful$', re.I)
    respectable_re = re.compile(r'respectable$', re.I)
    # s
    # t
    # u
    # v
    # w
    # x
    # y

    you_re = re.compile(r'you$', re.I)

    # z


    #
    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # a
    # b
    # c
    # d
    # e
    # f
    # g
    # h
    # i
    # j
    # k
    # l
    # m
    if man_re.search(word):
        man.man()
    # n
    # o
    # p
    # q
    # r
    elif respect_re.search(word):
        respect.respect()
    elif respectful_re.search(word):
        respectful.respectful()
    elif respectable_re.search(word):
        respectable.respectable()
    # s
    # t
    # u
    # v
    # w
    # x
    # y
    elif you_re.search(word):
        you.you()
    # z
    #
    else:
        print('not found...')
