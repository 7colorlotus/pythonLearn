#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量
# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


if __name__ == '__main__':
    student = Student('lotus')
    print("student.name: ", student.name)

    student.score = 90
    print("student.score: ", student.score)

    student2 = Student('jason')
    print("Student.count : ", Student.count)

    print("hasattr(student2, 'score') : ", hasattr(student2, 'score'))
