class Student:
    school = 'sc'
    obj_num = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = 'no_choose'
        Student.obj_num += 1

    def set_info(self, x, y, z):
        self.name = x
        self.age = y
        self.gender = z

    def print_info(self):
        print(self.name, self.age, self.gender, self.course)

    def choose(self, c_name):
        print('select class')
        self.course = c_name



s = Student('ll', 11, 'male')
# print(s.name)
# print(s.age)
# print(s.gender)
# 类中存储的对象共有的数据和功能
# 类可以访问
# 数据属性
# print(s.school)
# 函数属性
# print(s.set_info)
# print(s.print_info)

# 类的数据属性是共享给所有属性使用的 访问地址都一样
s2 = Student('ll2', 19, 'female')
# print(id(s.school))
# print(id(s2.school))
#
# Student.school = 'sc_2'
# print(s.school)
# print(s2.school)
#
# s.school = 'sc_2'
# print(s.school)
# print(s2.school)
# print(s.obj_num)

# 类的函数属性是绑定给对象用的

# 从类的角度调用
Student.print_info(s)
Student.set_info(s, 'lll', 10, 'female')
Student.print_info(s)
print(Student.print_info)

# 从对象调用
print(s.print_info)
print(s2.print_info)

# <function Student.print_info at 0x0000028630869E50>
# <bound method Student.print_info of <__main__.Student object at 0x0000028630878FD0>>
# <bound method Student.print_info of <__main__.Student object at 0x0000028630878F70>>
# 对于类调用是函数
# 对于对象调用是绑定方法 谁来调用就把谁当作的第一个参数传入
# 绑定给谁就是操作谁

s.choose('math')
s.print_info()
s2.print_info()

"""
python3中统一类与类型的概念
"""
