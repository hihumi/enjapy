#!/usr/bin/env python3


"""enjapy

main.py
主にユーザからの入力を担う
"""


from re_word import re_word


def main():
    """ユーザからの入力を担う関数。
    """

    print('enjapy:')
    print()
    print('英単語の意味を日本語で出力します。')
    print('以下に、調べたい英単語を入力してください。')
    print('(終了する場合は、q, またはQキーを入力してください。)')
    print('>>> ', end='')
    while True:
        word = input()

        if word == 'q' or word == 'Q':
            print('See you!')
            break

        re_word.re_word(word)

        print('>>> ', end='')

if __name__ == '__main__':
    main()