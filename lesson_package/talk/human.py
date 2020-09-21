# 絶対パスと相対パス 相対パスは非推奨(わかりづらい)
from lesson_package.tools import say
from ..tools import say


def sing():
    return 'sing'


def cry():
    return say.say_third('cry')