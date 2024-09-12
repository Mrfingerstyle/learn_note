class School:
    def __init__(self, nick_name, addr):
        self.nick_name = nick_name
        self.addr = addr
        self.classes = []

    def relate_class(self, class_obj):
        self.classes.append(class_obj)

    def tell_class(self):
        print(self.nick_name)
        for class_obj in self.classes:
            class_obj.tell_course()

class Class:
    def __init__(self, name):
        self.name = name
        self.course = None

    def relate_course(self, course_obj):
        self.course = course_obj

    def tell_course(self):
        print(self.name)
        self.course.tell_info()

class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        print(self.name, self.period, self.price)

s_1 = School('sc_1', 'sh')
s_2 = School('sc_1', 'bj')

class_obj_1 = Class('14')
class_obj_2 = Class('15')

s_1.relate_class(class_obj_1)
s_2.relate_class(class_obj_2)

c1 = Course('python', '6', '10000')
c2 = Course('java', '12', '20000')

class_obj_1.relate_course(c1)
class_obj_2.relate_course(c2)

print('-' * 50)
class_obj_1.tell_course()
class_obj_2.tell_course()

print('-' * 50)
s_1.tell_class()
s_2.tell_class()



