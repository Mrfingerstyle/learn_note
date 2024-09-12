# 类 先定义再调用
# 类体代码在定义阶段立即执行 会产生类的名称空间

class Student:
    school = 'sc'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_info(self):
        pass

    def print_info(self):
        pass

    print('-'*10)

# s = Student('ll', 19, 'male')
# print(s.school)

# 类的名称空间
print(Student.__dict__)


# 访问类属性
print(Student.school)

# 访问实例属性
print(Student.print_info)


