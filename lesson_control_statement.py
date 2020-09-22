# 制御文

# 空か否かの判定
is_ok = True
is_ok = "akldjadjf"
is_ok = 0
is_ok = ''
is_ok = []
if is_ok:
    print('OK!')
else:
    print('NO!')

is_empty = None
print(is_empty)
if is_empty == None:
    print('None!')
if is_empty is not None:
    print('Not None!')

# オブジェクトの判定
print(1 == True)
print(1 is True)

# while else構文
count = 0
while count < 5:
    # if count == 1:
    #    break
    print(count)
    count += 1
else:
    print('done')

# input関数
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('Next')

for i in 'abcdefg':
    print(i)

for word in ['My', 'name', 'is', 'Mike']:
    if word is 'name':
        break
    print(word)

# boolean型の判定
is_ok = False
if not is_ok:
    print('not ok!')

# range関数
for i in range(2, 10, 2):
    print(i)

# range関数でiteratorを参照する必要がない場合
for _ in range(5):
    print('hey!')

# enumerate関数
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(i, fruit)

# zip関数を用いた複数のリストの値を同時参照
days = ['Mon', 'Tue', 'Wed']
drinks = ['coffee', 'tea', 'beer']
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# 関数の定義にtypehintを入れる
def add_num(a: int, b: int) -> int:
    return a + b


print(add_num(10, 20))
# typehintは別の型が入ってもエラーを吐かない
print(add_num('a', 'b'))


# 関数の引数は順序が重要
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)


menu('beef', 'ice', 'beer')
menu(entree='beef', dessert='ice', drink='beer')
menu('beef', dessert='ice', drink='beer')


# デフォルト引数を用いた関数
def menu2(entree='chicken', drink='coffee', dessert='cake'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)


menu2()


# デフォルト引数は参照渡しになる
def test_func(x, l=[]):
    l.append(x)
    return l


print(test_func(100))
print(test_func(100))


def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


print(test_func2(100))
print(test_func2(100))


# 位置引数のタプル化
def say_somthing(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)


say_somthing('hoge', 'fuga', 'fugafuga')
# tupleを*で明示して使える
test_tuple = ('test', 'testtest')
say_somthing('hoge', *test_tuple)


# キーワード引数の辞書化
def menu_kwargs(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, ':', v)


menu_kwargs(entree='beef', drink='coffee')
dict_sample = {'entree': 'fish', 'drink': 'tea', 'dessert': 'ice'}
menu_kwargs(**dict_sample)


# Docstrings of Google format
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (str): The first parameter.
        param2 (str): The first parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True


print(example_func('hoge', 'fuga'))
# Docstringsの表示
print(example_func.__doc__)
help(example_func)


# 関数内関数
def outer(a, b):
    def sub(c, d):
        return c - d

    print(sub(a, b))
    print(sub(b, a))


outer(1, 2)


# クロージャー
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius ** 2

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.1415926535)

print(ca1(10))
print(ca2(10))


# デコレーター
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


def add_num(a, b):
    return a + b


f = print_info(add_num)
r = f(10, 20)
print(r)


# @でデコレーターを使う 複数使う場合は順序を気にする
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


@print_info
@print_more
def add_num2(a, b):
    return a + b


r = add_num2(10, 20)

# ラムダ functionを引数にする場合に使える
days = ['Sun', 'mon', 'tue', 'Wed', 'Thu', 'fri', 'sat']


def change_words(words, func):
    for word in words:
        print(func(word))


change_words(days, lambda word: word.capitalize())
change_words(days, lambda word: word.lower())


# ジェネレーター 重たい処理を分割して、呼び出す度に実行する
def counter(num=10):
    for _ in range(num):
        yield 'run'


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
c = counter()
print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

r1 = [i for i in t if i % 2 == 0]
print(r1)
# 下の例は可読性が低いのであまり使わない
r2 = [i * j for i in t for j in t2]
print(r2)

# 辞書内包表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
s = {i for i in range(10)}
print(s)

# ジェネレーター内包表記
g = (i for i in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# ジェネレーターをfor文で実行する
for x in g:
    print(x)

# タプル内包表記
t = tuple(i for i in range(10))
print(t)

# 名前空間とスコープ
animal = 'cat'


def f():
    # global変数の書き換え
    global animal
    animal = 'dog'
    plant = 'rose'
    print(animal)
    # local変数の表示
    print('locals:', locals())


f()
# global変数の表示
print('globals', globals())

# 例外処理
l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as ex:
    print(f'Don\'t worry: {ex}')
except NameError as ex:
    print(ex)
except Exception as ex:
    print(f'other: {ex}')
else:
    print("done")
# 最後に実行したい処理を書く
finally:
    print('Clean up')


# 独自例外の作成
class UpperCaseError(Exception):
    pass


def check():
    words = ['apple', 'BANANA', 'orange']
    for word in words:
        if word.isupper():
            raise UpperCaseError


#check()
try:
    check()
except UpperCaseError as e:
    print("This error is my fault.")