#!/use/bin/env python3


"""checkの日本語意味を出力する
"""


def check_ja_func():
    """checkの日本語意味を出力する関数

    doctest:
    >>> check_ja_func()
    check:
    [動]: (1) ...を調べる, 確かめる (2) ...を照合する (3) (速度等)を阻止する, (感情等)を抑制する (備考: checkは自動詞としても使用できる)
    [名]: (1) 検査 (2) 勘定書 (3) 小切手
    """

    print('check:')

    check_ja_words = """[動]: (1) ...を調べる, 確かめる (2) ...を照合する (3) (速度等)を阻止する, (感情等)を抑制する (備考: checkは自動詞としても使用できる)
[名]: (1) 検査 (2) 勘定書 (3) 小切手"""

    print(check_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    check_ja_func()
