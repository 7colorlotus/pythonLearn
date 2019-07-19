#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types


def fn():
    pass


# 使用type判断类型
def use_type():
    # 查看对象类型
    print(type(123))

    print(type('str'))

    print(type(1.5))

    print(type(None))

    # 函数类型
    print(type(abs))

    print("type('123') == type('456') ? ", type('123') == type('456'))

    # 判断一个对象是否是函数
    print("type(fn) == types.FunctionType ?", type(fn) == types.FunctionType)
    # 判断lambda匿名函数
    print("type(lambda x: x * x) == types.LambdaType ?", type(lambda x: x * x) == types.LambdaType)
    # 自动生成的类型
    print("type(x for x in range(1,10)) == types.GeneratorType ? ",
          type(x for x in range(1, 10)) == types.GeneratorType)


# 优先使用isinstance()判断类型
def use_isinstance():
    print("isinstance(1,int) ? ", isinstance(1, int))
    print("isinstance('abc', str) ? ", isinstance('abc', str))

    print("[1, 3, 2], (list, tuple))", isinstance( [1, 3, 2], (list, tuple)))
    print("(1, 3, 2), (list, tuple))", isinstance((1, 3, 2), (list, tuple)))


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
def use_dir():
    print("dir('abc'): \n", dir('abc'))
    print("len('abc'): ", len('abc'))
    print("'abc'.__len__(): ", 'abc'.__len__())


# 自定义一个类，实现__len__方法,然后可以使用len()调用
class MyObj(object):
    def __init__(self, val):
        self.val = val

    def __len__(self):
        return self.val.__len__()

    @staticmethod
    def hi():
        print("static method hello")


if __name__ == '__main__':
    use_dir()

    myObj = MyObj('hello')
    print("myObj.__len__() : ", myObj.__len__())
    print("len(myObj) : ", len(myObj))

    setattr(myObj, 'x', 99)
    print("hasattr(myObj, 'x') : ", hasattr(myObj, 'x'))

    MyObj.hi()

    print(hasattr(myObj, 'hi'))

    if(hasattr(myObj, 'hi')):
        myObj.hi()


