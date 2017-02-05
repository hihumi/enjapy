#!/usr/bin/env python3


"""enjapy

main.py
主にユーザからの入力を担う
"""


from re_en.re_search_en import re_search_en_func


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
        try:
            word = input()

        except (TypeError, ValueError) as err:
            print('Error: {} おっと、エラーです。半角アルファベットで入力してください。'.format(err))

        else:
            if word == 'q' or word == 'Q':
                print('See you!')
                break

            re_search_en_func(word)

            print('>>> ', end='')

if __name__ == '__main__':
    main()
