"""
多态 同一事物有多种形态
多态性 在不考虑对象具体类型的情况下直接使用对象
"""
# class Animal:
#     @staticmethod
#     def say(self):
#         print('say somthing')
#
# class People(Animal):
#     def say(self):
#         print('People say somthing')
#
# class Dog(Animal):
#     def say(self):
#         print('Dog say somthing')
#
# class Pig(Animal):
#     def say(self):
#         print('Pig say somthing')

# obj_1 = People()
# obj_2 = Dog()
# obj_3 = Pig()

# obj_1.say()
# obj_2.say()
# obj_3.say()

# 这三个类可以没有关系 只要定义了say 也可以被统一的接口调用
# class People:
#     def say(self):
#         print('People say somthing')
#
# class Dog:
#     def say(self):
#         print('Dog say somthing')
#
# class Pig:
#     def say(self):
#         print('Pig say somthing')
#
# # 定义统一的接口 接收传入的动物对象
# def animal_say(animal):
#     animal.say()
# obj_1 = People()
# obj_2 = Dog()
# obj_3 = Pig()
# animal_say(obj_1)
# animal_say(obj_2)
# animal_say(obj_3)
#
# # 例如len()
# print(len('123'))
# print(len([1, 2, 3]))
# print('123'.__len__())
#
# def my_len(val):
#     return val.__len__()
#
# print(my_len('123'))

# 例如 linux一切接文件的概念 也就是多态性的思想
# class Cpu:
#     def read(self):
#         print('cpu read')
#
#     def write(self):
#         print('cpu write')
#
#
# class Mem:
#     def read(self):
#         print('Mem read')
#
#     def write(self):
#         print('Mem write')
#
#
# class Txt:
#     def read(self):
#         print('Txt read')
#
#     def write(self):
#         print('Txt write')
#
# obj1 = Cpu()
# obj2 = Mem()
# obj3 = Txt()
#
# obj1.read()
# obj1.write()
#
# obj2.read()
# obj2.write()

# 父类有时候的作用是定义一个规范 约定子类中必须含有哪些方法
import abc
# 统一所有子类的标准 类似其他语言接口的概念
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass

# 不能实例化抽象类自己
# obj = Animal()

class People(Animal):
    # 此时继承父类 必须定义say
    def say(self):
        print('People say somthing')
    # pass

class Dog(Animal):
    def say(self):
        print('Dog say somthing')

class Pig(Animal):
    def say(self):
        print('Pig say somthing')

a = People()
a.say()
