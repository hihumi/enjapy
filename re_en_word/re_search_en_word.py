#!/usr/bin/env python3


"""このスクリプトは、main.pyで入力されたwordの正規表現をチェックする。
"""


import re

# a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from print_ja_word ~
# a
from print_ja_word.a_ja import a_ja_func
# i
from print_ja_word.individual_ja import individual_ja_func
from print_ja_word.individuality_ja import individuality_ja_func

# r
from print_ja_word.respect_ja import respect_ja_func
from print_ja_word.respectful_ja import respectful_ja_func
from print_ja_word.respectable_ja import respectable_ja_func


# w
from print_ja_word.will_ja import will_ja_func
from print_ja_word.willpower_ja import willpower_ja_func

# y
from print_ja_word.you_ja import you_ja_func

# re.compile関係
from re_en_word.a_re import a_re_func
# re.compileの関数化test
# def a_re():
#     a_re = re.compile(r'a$', re.I)
#     return a_re


def re_search_en_word(word):
    """この関数は、main.pyで入力されたwordが、正規表現に合致するかどうか調べ、
    dir: print_wordにある各関数を呼び出す。
    """


    # TODO: re.compile関係を関数化すること
    # a_re = a_re_func() # これはいらない
    # これでいい
    # if a_re_func().search(word):
    #     a_ja_func()
    # re.compile:
    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # a
    #a_re = re.compile(r'a$', re.I)
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
    if a_re_func().search(word):
        a_ja_func()
    # b
    # c
    # d
    # e
    # f
    # g
    # h
    # i
    elif individual_re.search(word):
        individual_ja_func()
    elif individuality_re.search(word):
        individuality_ja_func()
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
        respect_ja_func()
    elif respectful_re.search(word):
        respectful_ja_func()
    elif respectable_re.search(word):
        respectable_ja_func()
    # s
    # t
    # u
    # v
    # w
    elif will_re.search(word):
        will_ja_func()
    elif willpower_re.search(word):
        willpower_ja_func()
    # x
    # y
    elif you_re.search(word):
        you_ja_func()
    # z
    #
    else:
        print('not found...')
