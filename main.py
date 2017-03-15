#!/usr/bin/env python3


"""enjapy

main.py
主にユーザからの入力を担う
"""


import re

#from re_en.re_search_en import re_search_en_func

# a b c d e f g h i j k l m n o p q r s t u v w x y z
#
# from re_en.char_Char_re_search_en import char_Char_re_search_en_func
# a:
from re_search_en.a_A_re_search_en import a_A_re_search_en_func
# c: c_C_re_search_en_func
from re_search_en.c_C_re_search_en import c_C_re_search_en_func
# i:
from re_search_en.i_I_re_search_en import i_I_re_search_en_func
# m:
from re_search_en.m_M_re_search_en import m_M_re_search_en_func
# n:
from re_search_en.n_N_re_search_en import n_N_re_search_en_func
# o:
from re_search_en.o_O_re_search_en import o_O_re_search_en_func
# p:
from re_search_en.p_P_re_search_en import p_P_re_search_en_func
# r:
from re_search_en.r_R_re_search_en import r_R_re_search_en_func
# s:
from re_search_en.s_S_re_search_en import s_S_re_search_en_func
# w:
from re_search_en.w_W_re_search_en import w_W_re_search_en_func


def main():
    """ユーザからの入力を担う関数
    """

    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    #
    # char_Char_re = re.compile(r'^char', re.I)
    # a:
    a_A_re = re.compile(r'^a', re.I)
    # c:
    c_C_re = re.compile(r'^c', re.I)
    # i:
    i_I_re = re.compile(r'^i', re.I)
    # m:
    m_M_re = re.compile(r'^m', re.I)
    # n:
    n_N_re = re.compile(r'^n', re.I)
    # o:
    o_O_re = re.compile(r'^o', re.I)
    # p:
    p_P_re = re.compile(r'^p', re.I)
    # r:
    r_R_re = re.compile(r'^r', re.I)
    # s:
    s_S_re = re.compile(r'^s', re.I)
    # w:
    w_W_re = re.compile(r'^w', re.I)


    print('enjapy:')
    print('Welcome!')
    print()
    print('英単語の意味を日本語で出力します。')
    print('以下に、調べたい英単語を入力してください。')
    print('(終了する場合は、0を入力してください。)')
    print('>>> ', end='')
    while True:
        try:
            word_strip = input().strip()

        except (TypeError, ValueError) as err:
            print('Error: {} おっと、エラーです。半角アルファベットで入力してください。'.format(err))

        else:
            if word_strip == '0':
                print('See you!')
                break

            # a b c d e f g h i j k l m n o p q r s t u v w x y z
            #
            # elif char_Char_re.search(word_strip): # char:
            #    char_Char_re_search_en_func(word_strip)
            #
            if a_A_re.search(word_strip): # a
                a_A_re_search_en_func(word_strip)
            elif c_C_re.search(word_strip): # c
                c_C_re_search_en_func(word_strip)
            elif i_I_re.search(word_strip): # i
                i_I_re_search_en_func(word_strip)
            elif m_M_re.search(word_strip): # m
                m_M_re_search_en_func(word_strip)
            elif n_N_re.search(word_strip): # n
                n_N_re_search_en_func(word_strip)
            elif o_O_re.search(word_strip): # o
                o_O_re_search_en_func(word_strip)
            elif p_P_re.search(word_strip): # p
                p_P_re_search_en_func(word_strip)
            elif r_R_re.search(word_strip): # r
                r_R_re_search_en_func(word_strip)
            elif s_S_re.search(word_strip): # s
                s_S_re_search_en_func(word_strip)
            elif w_W_re.search(word_strip): # w
                w_W_re_search_en_func(word_strip)
            else:
                print('not found...')

            print('>>> ', end='')

if __name__ == '__main__':
    main()
