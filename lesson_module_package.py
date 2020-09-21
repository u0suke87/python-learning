import sys

# 　実行時引数の読み込み
print(sys.argv)

# 自作パッケージ
import lesson_package.utils
# from lesson_package.utils import say_twice
from lesson_package import utils

r = utils.say_twice('hello')
print(r)


from lesson_package.talk import human
r = human.sing()
print(r)

# 絶対パスと相対パスは lesson_package/talk/human.py を参照
r = human.cry()
print(r)


# package内の全てのmoduleのimport
# *を使うには、読み込むpackageの__init__.pyに__all__でファイル名のリストを定義する
# *は非推奨 何を読み込んで使いたいのか不明瞭
from lesson_package.talk import *
r = animal.cry()
print(r)

# 古いパッケージと新しいパッケージのバージョンがある場合に使用する。
try:
    from lesson_package.tools import utils
except ImportError:
    from lesson_package import utils

print(utils.say_twice('word'))

# importする際の記述順序
# 1.標準パッケージ、サードパーティーパッケージ、自作パッケージの順で空行を入れる
# 2.各パッケージ群はa-zの名前の昇順でimportする
import collections
import os
import sys

import termcolor

import config
import lesson_package

# packageのpathを表示する
print(config.__file__)
print(lesson_package.__file__)
# packageでimportできるpath
print(sys.path)

# __name__と__main__
# 呼び出し元のpythonファイルである場合、__name__に__main__が入る
print('main:', __name__)


# 本来であれば、main関数は以下のように明示する。
# また、packageとして扱われてもhogehoge()が実行されないように処理を書く。
def main():
    hogehoge()

if __name__ == '__main__':
    main()