class Student:
    school = 'sc'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_info(self, x, y, z):
        self.name = x
        self.age = y
        self.gender = z

    def print_info(self):
        print(self.name, self.age, self.gender)


# 调用类产生对象
s = Student('ll', 18, 'male')
s.print_info()

# 本质是操作名称空间
s.num = 1
print(s.__dict__)
