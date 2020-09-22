# Classの定義で、python3から引数は省略できるが、継承元を明らかにした方が良い。
class Person(object):
    # コンストラクタ
    def __init__(self, name='default_name', age=1):
        self.name = name
        self.age = age

    def say_somthing(self):
        print(f'I am {self.name}. hello')
        self.run(10)

    def run(self, num):
        print('run!' * num)

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

    # デストラクタ
    def __del__(self):
        print('good bye')


class Person2:
    def say_somthing(self):
        print('hello')


person = Person('Mike')
person.say_somthing()
person2 = Person2()
person2.say_somthing()

# デストラクタの起動。明示して削除しない場合は全ての処理が終了した後にデストラクタが起動する
del person


# クラスの継承
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


class ToyotaCar(Car):
    # runメソッドは自動継承
    pass


class TeslaCar(Car):
    # コンストラクタのオーバーライドと、オーバーライド元のメソッドの継承
    def __init__(self, model='Model S',
                 enable_auto_run='False',
                 passwd='123'):
        # self.model = model
        super().__init__(model)
        # propertyにはアンダースコアをつける
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # 読み込みは可能で、書き込みは不可能にする(=getter)
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # 書き込みを可能にする(基本的には条件付きで書き込みを可能にする場合に使用する。条件がない場合、そもそも@propertyをつけなければ良い)
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    # runメソッドのオーバーライド
    def run(self):
        print('fast run')

    def auto_run(self):
        print('auto_run')


car = Car()
car.run()
print('##########')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('##########')
# tesla_car = TeslaCar(model='Model S')
tesla_car = TeslaCar(model='Model S', passwd='456')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
print('##########')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

# propertyの命名規則
# アンダースコアがない(e.g. self.enable_auto_run)場合、クラスの外からでも自由に書き換えて良い
# アンダースコアが一つ(e.g. self._enable_auto_run)の場合、基本的にはクラスの外から書き換えられたくないけど、setter使って書き換えても良い場合
# アンダースコアが二つ(e.g. self.__enable_auto_run)の場合、クラスの外部からアクセスできない。


# クラスを構造体として扱う
class T(object):
    pass


t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

# 上記のようにクラスは構造体として扱える一方、本来アクセスできないはずのメンバにあたかもアクセスできたように見えてしまう場合がある
# 例えば、__attributeはクラス外から見えないはずだが、構造体としてクラス外で定義するとクラスにアクセスできたかのように見えてしまう。
tesla_car.__enable_auto_run = 'testtest'
print(tesla_car.__enable_auto_run)


# duck typing
class Baby(Person):
    def __init__(self, name='default_name', age=1):
        if age < 18:
            super().__init__(name=name, age=age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, name='default_name', age=18):
        if age >= 18:
            super().__init__(name=name, age=age)
        else:
            raise ValueError


baby = Baby()
adult = Adult()
car = Car()
# car.ride(baby)
car.ride(adult)


# 抽象クラスはpythonではabcパッケージをimportして実装する。コードスタイルとして、抽象クラスは必要がなければ実装しなくても良い。
import abc


class Human(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def say_hello(self):
        pass


class Japanese(Human):
    def say_hello(self):
        print('konnichiwa')


class American(Human):
    # pass # say_helloを実装しないとエラーが出力される
    def say_hello(self):
        print('hello')


japanese = Japanese()
american = American()


# 多重継承。最初から多重継承しないように設計できるなら多重継承は使わない方が良い。
# 継承元の関数に同じ名前のメソッドがあった場合、継承先のクラス宣言時に引数としてより左に書いた継承元クラスのメソッドが継承される。
class Person(object):
    def talk(self):
        print('talk')
    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('car run')


class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()


# クラス変数 どのオブジェクトでも共通で使うメンバの定義
class Person(object):
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


# クラス変数はリストの場合、オブジェクト作成時に初期化されない。全てのオブジェクトで共通に使われる
class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)
d = T()
d.add_word('add 3')
d.add_word('add 4')
print(c.words)


# クラスの中でリストを初期化してメンバとして持ちたい場合は、コンストラクタの中で行う
class T2(object):
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)


e = T2()
e.add_word('add 1')
e.add_word('add 2')
print(e.words)
f = T2()
f.add_word('add 3')
f.add_word('add 4')
print(e.words)


# クラスメソッドとスタティックメソッド
class Person(object):
    kind = 'humnan'

    def __init__(self):
        self.x = 100

    # クラスメソッド オブジェクトを作成しなくても呼び出せる。クラス内のクラス変数を参照した処理を書ける。
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # スタティックメソッド あまり使う機会はない
    @staticmethod
    def about(year):
        print(f'about human {year}')


a = Person()
print('a:', a.x)
print('a:', a.kind)
b = Person
# bはオブジェクトではないのでメンバxは初期化されておらず、参照できない
# print('b:', b.x)
# 一方、クラス変数にはアクセスできる
print('b:', b.kind)

print('class method:', Person.what_is_your_kind())
Person.about(1993)


# 特殊メソッド
class Word():

    def __init__(self, text):
        self.text = text

    # オブジェクトがstrとして呼ばれた際に値を返す特殊メソッド
    def __str__(self):
        return 'word!!!!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word2):
        return self.text.capitalize() + word2.text.capitalize()

    def __eq__(self, word2):
        return self.text == word2.text


word = Word('test')
print(word)
# 特殊メソッドにより、オブジェクトのtextの長さが取得できる
print(len(word))
print(len(word.text))

word2 = Word('test')
# 特殊メソッドにより、オブジェクトの連結ができる
print(word + word2)
print(word.text + word2.text)
# 特殊メソッドにより、オブジェクト自体ではなく、オブジェクトのtextが比較できるようになる
print(word == word2)
print(word.text == word2.text)