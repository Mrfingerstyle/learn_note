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

    def relate_course(self, course_name):
        self.course = course_name

    def tell_course(self):
        print(self.name, self.course)

class_obj_1 = Class('14')
class_obj_2 = Class('15')

class_obj_1.relate_course('python')
class_obj_2.relate_course('linux')

s_1 = School('sc_1', 'sh')
s_2 = School('sc_1', 'bj')

s_1.relate_class(class_obj_1)
s_2.relate_class(class_obj_2)

s_1.tell_class()
s_2.tell_class()
