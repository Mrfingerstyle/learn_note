"""
绑定方法
    绑定给对象的方法 调用者是对象 自动传入的是对象
    绑定给类的方法 调用者是类 自动传入的是类

非绑定方法 静态方法
    没有绑定给特定
    调用者可以是象或类调用 没有自动传参的效果
    使用场景 类体代码不需要类或对象
"""
import uuid


class Mysql:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # 将下述方法装饰成一个静态方法
    # 没有自动传参
    # 可以自定义参数
    @staticmethod
    def create_id():
        import uuid
        return uuid.uuid4()

obj = Mysql('127', 3306)
# <function Mysql.create_id at 0x00000272B63795E0>
print(obj.create_id)
print(Mysql.create_id)
print(obj.create_id())
print(Mysql.create_id())

