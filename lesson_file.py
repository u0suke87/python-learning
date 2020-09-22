f = open('test.txt', 'w')
# f = open('test.txt', 'a')
f.write('Test\n')
print('My', 'name', 'is', 'Mike', file=f)
f.close()

# 上記をインデントを利用して、メモリを消費しないように利用後に閉じる
with open('test.txt', 'w') as f:
    f.write('test\n')
    print('My', 'name', 'is', 'Mike', file=f)

s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as f:
    # 全文読み込み
    # print(f.read())
    while True:
        # 一行ずつ読み込み
        # line = f.readline()

        # chunkで指定した文字数ごとに読み込み
        chunk = 2
        line = f.read(chunk)

        print(line, end='')
        if not line:
            break

# seekを使用して、読み込んでいるファイルで見る位置を移動する
# 改行も1文字に含める
with open('test.txt', 'r') as f:
    # 今ファイルの先頭行から何文字目にいるか
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    print(f.read(1))
    # ファイルの先頭から14文字目に移動する。(最初の文字を0文字目とカウントして)
    f.seek(14)
    print(f.read(1))
    # ファイルの先頭から15文字目に移動する。(最初の文字を0文字目とカウントして)
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))

# 書き込みと読み込みを同時にやる
# 書き込んでから読み込み'w+'
# 読み込んでから書き込み'r+'
with open('test.txt', 'w+') as f:
    f.write(s)
    # 書き込んだ後は最終文字の次を示す
    print(f.tell())
    f.seek(0)
    print(f.read())

# テンプレートの使用
# 誤操作によって、エンジニアが書き換えてしまいたくない場合に使用できる
import string

email_template = """\

Hi $name.

How are you?

$content
"""

with open('design/email_template.txt', 'w') as f:
    f.write(email_template)

# with句の中で代入したtは、with句の外でも使用できる
with open('design/email_template.txt', 'r') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', content='Have a good day.')
print(contents)


import csv

with open('test.csv', 'w') as csv_file:
    field_names = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': '1'})
    writer.writerow({'Name': 'B', 'Count': '2'})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])


import os

print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('design'))

# ファイルのリネーム
os.rename('test.txt', 'renamed.txt')
# シンボリックリンク作成 (何回も実行するとファイルが既に存在すると怒られるので消しておく)
if os.path.exists('symlink.txt'):
    os.remove('symlink.txt')
os.symlink('renamed.txt', 'symlink.txt')
# ディレクトリの作成
if os.path.exists('test_dir'):
    os.rmdir('test_dir')
os.mkdir('test_dir')

import pathlib

# 空ファイルの作成
pathlib.Path('empty.txt').touch()
os.remove('empty.txt')

# ls ディレクトリに関して
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))


import glob

# ls ファイルに関して
pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))


import shutil

# ファイルのコピー
shutil.copy('test_dir/test_dir2/empty.txt',
            'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))

# 全てのフォルダの削除
shutil.rmtree('test_dir')

# カレントディレクトリの取得
print(os.getcwd())


# tarfileを使う
import tarfile
os.mkdir('test_dir')
os.mkdir('test_dir/sub_dir')
with open('test_dir/sub_dir/sub.txt', 'w') as f:
    f.write('sub')

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tarファイルの展開
    tr.extractall(path='test_tar')
    # tarファイルを展開せずに確認
    with tr.extractfile('test_dir/sub_dir/sub.txt') as f:
        print(f.read())

shutil.rmtree('test_dir')
shutil.rmtree('test_tar')
os.remove('test.tar.gz')

# gitにコミットしたくないファイル削除
os.remove('renamed.txt')
os.remove('symlink.txt')
os.remove('test.csv')


import zipfile

# zipファイルの作成
with zipfile.ZipFile('test.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive=True):
        #print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')
    with z.open('test_dir/test.txt') as f:
        print(f.read())

import tempfile


with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# temporaryファイルを作成して、消したく無い場合
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時的にフォルダを作成して、その中で圧縮したりという用途に用いる
with tempfile.TemporaryDirectory() as td:
    print(td)

# temporaryディレクトリを作成して、消したく無い場合
temp_dir = tempfile.mkdtemp()
print(temp_dir)


# ターミナルコマンドをpython上から行う
import subprocess


# os.systemでもできるが非推奨、subprocessの方が高機能なので
# os.system('ls')
subprocess.run(['ls', '-al'])

# 上記はリストで渡しているが、shell=Trueとするとパイプも使える
# shellインジェクションを防ぐために非推奨
subprocess.run('ls -al | grep lesson', shell=True)

# reterncodeを利用すると、例外処理ができる
r = subprocess.run('lsa', shell=True)
print(r.returncode)


print('######')
# shell=Trueとせずにパイプを使用する場合
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'lesson'],
                      stdin=p1.stdout,
                      stdout=subprocess.PIPE)
p1.stdout.close()
# 出力がリストで渡される
output = p2.communicate()
print(output)

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
now_time = now.strftime('%Y-%m-%d')
print(now_time)


import time

print('###')
time.sleep(2)
print('###')
print(time.time())

import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, f'{file_name}_{now_time}')

with open(file_name, 'w') as f:
    f.write('test')
