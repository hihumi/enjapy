#!/use/bin/env python3


"""planの日本語意味を出力する
"""


def plan_ja_func():
    """planの日本語意味を出力する関数

    doctest:
    >>> plan_ja_func()
    plan:
    <BLANKLINE>
        [名] [C] (1) (しばしば複数形で)計画, 予定, 案
        (2) (組織等の)事業計画, 活動予定
        (3) 計画図, 図面, 設計図, 配置図, (小区画の)地図
    <BLANKLINE>
        [動] [他] (1) ...の計画を立てる (2) ...するつもりである
        (3) ...の設計図を書く
        [自] (1) 計画を立てる (3) ...するつもりである
    """

    print('plan:')
    print()

    plan_ja_words = """    [名] [C] (1) (しばしば複数形で)計画, 予定, 案
    (2) (組織等の)事業計画, 活動予定
    (3) 計画図, 図面, 設計図, 配置図, (小区画の)地図

    [動] [他] (1) ...の計画を立てる (2) ...するつもりである
    (3) ...の設計図を書く
    [自] (1) 計画を立てる (3) ...するつもりである"""

    print(plan_ja_words)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    plan_ja_func()
