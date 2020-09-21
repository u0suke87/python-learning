# 型宣言
from typing import List

name: str = 'Mike'

# print関数のTips
print('Hi', name, sep=', ', end='.\n')

# べき乗、丸め誤差
print(round(5.1 ** 3, 2))

import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# raw文字列
print('C:\name\name')
print(r'C:\name\name')

# 複数行にまたがる改行
print('#########')
print("""\
line1
line2
line3\
""")
print('#########')

# 複数回同じ文字列を表示する
print('Hi.' * 3 + 'Mike')

# 文字列の連結
s1 = 'aaaaaaaaa' \
     'bbbbbbbbb'
s2 = ('aaaaaaaaa'
      'bbbbbbbbb')
print(s1)
print(s2)

# 文字列のインデックスとスライス
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
print(word[:])
# 文字列のインデックスに代入はできない！
# word[0] = 'j'
word = 'j' + word[1:]
print(word)

# 文字列のメソッド
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

# f-format
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')

# リスト
l = list('abcdefg')
print(l)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 最初を0番目として、1番目から１個飛ばしで取得
print(n[1::2])
# 最後から取得
print(n[::-1])
# リストの間を削除
l = [1, 2, 3, 4, 5, 6]
print(l[1:3])
l[1:3] = [7, 8]
print(l)
l[1:3] = []
print(l)

# リストに値を追加/削除
n.append(100)
n.insert(0, 200)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(a + b)
a += b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)

# indexを取得する
print(x.index(6))
# 3番目のindexから検索する
print(a.index(6, 3))

# リストのソート
r = [1, 2, 3, 4, 5, 1, 2, 3]
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
x = ' '.join(to_split)
print(x)

# 参照渡し 先頭アドレス
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j, ' id=', id(j))
print('i =', i, ' id=', id(i))

# 値渡し
x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:] #or
y[0] = 100
print(x)
print(y)

# tuple 読み込み用途のリスト 宣言時から変更できない
t1 = (1, 2, 3)
t2 = 1, 2, 3
print(type(t1))
print(type(t2))
t3 = 1,
t4 = (1)
print(type(t3))
print(type(t4))
new_tuple = t3 + (2, 3, 4,)
print(new_tuple)

# タプルを展開した宣言
num_tuple = (10, 20)
x, y = num_tuple
print(x, y)
min, max = 0, 100
print(min, max)

# アンパックでswapする
i = 10
j = 20
print(i, j)
i, j = j, i
print(i, j)

# 辞書型
# update
d = {'x': 10, 'y': 20}
d2 = {'x': 1000, 'z': 30}
d.update(d2)
print(d)
# 値の取得
print(d.get('x'))
# keyの確認
print('x' in d)
# 中身の取り出し
d.pop('x')
print(d)
d.clear()
print(d)
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
y = x.copy()
y['a'] = 100
print(x, y)

# 集合 set
a = {1, 2, 3, 4, 5, 6}
print(type(a))
b = {2, 3, 3, 6, 7}
print(b)
print(a-b)
print(a & b)
print(a | b)
print(a ^ b)

s = {1, 2, 3, 4, 5, 6}
s.add(6)
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)
s1 = set()
print(type(s1))
s2 = {}
print(type(s2))


