class Student:
    school = 'sc'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 实例化
s = Student('ll', 19, 'male')

"""
实例化过程
    产生一个空对象
    调用init函数将传入的参数初始化
    返回初始完的对象
总结
    init在调用类时自动执行 用来为对象初始化自己独有的数据 默认返回None
    init内应该存放的是为对象初始化的功能 但是也可以存放其他代码
    类调用时立刻执行的代码都可以放在该方法内
"""
