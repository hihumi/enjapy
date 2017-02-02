#!/usr/bin/env python3


"""このスクリプトは、main.pyで入力されたwordの正規表現をチェックする。
"""


import re

# a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# a
from print_ja_word import a
# i
from print_ja_word import individual
from print_ja_word import individuality

# r
from print_ja_word import respect
from print_ja_word import respectful
from print_ja_word import respectable


# w
from print_ja_word import will
from print_ja_word import willpower

# y
from print_ja_word import you


def re_en_word(word):
    """この関数は、main.pyで入力されたwordが、正規表現に合致するかどうか調べ、
    dir: print_wordにある各関数を呼び出す。
    """

    # re.compile:
    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # a
    a_re = re.compile(r'a$', re.I)
    # b
    # c
    # d
    # e
    # f
    # g
    # h
    # i
    individual_re = re.compile(r'individual$', re.I)
    individuality_re = re.compile(r'individuality$', re.I)
    # j
    # k
    # l
    # m
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
    will_re = re.compile(r'will$', re.I)
    willpower_re = re.compile(r'willpower$', re.I)
    # x
    # y
    you_re = re.compile(r'you$', re.I)
    # z


    # re.search:
    #
    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # a
    if a_re.search(word):
        a.a()
    # b
    # c
    # d
    # e
    # f
    # g
    # h
    # i
    elif individual_re.search(word):
        individual.individual()
    elif individuality_re.search(word):
        individuality.individuality()
    # j
    # k
    # l
    # m
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
    elif will_re.search(word):
        will.will()
    elif willpower_re.search(word):
        willpower.willpower()
    # x
    # y
    elif you_re.search(word):
        you.you()
    # z
    #
    else:
        print('not found...')
