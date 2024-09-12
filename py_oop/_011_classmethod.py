"""
绑定方法
    绑定给对象的方法 调用者是对象 自动传入的是对象
    绑定给类的方法 调用者是类 自动传入的是类

非绑定方法

"""

IP = '127.0.0.1'
PORT = 3306

class Mysql:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # 将下面的函数装饰成绑定给类的方法
    @classmethod
    def from_conf(cls):
        # cls自动传入 指代当前的类
        print(cls)
        return cls(IP, PORT)


cls = Mysql.from_conf()
print(cls.__dict__)


