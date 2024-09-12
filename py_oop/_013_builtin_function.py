# 内置函数
# print(abs(-1))
# print(any([1, 'aaa', '1']))
# print(any([]))
#
# print(any([0, None, 1]))
# print(any([]))
#
# print(bin(11))
# print(oct(11))
# print(hex(11))
#
# print(bool(''))

# 检查类或方法是否可调用
print(callable(print))

class People:
    pass

print(callable(People))

p = People()
print(isinstance(p, People))

print(divmod(10, 3))

print('abc'.__repr__())
print('abc'.__str__())

print(round(1.2345, 2))

l1 = [1, 2, 3, 4, 5]
# slice()
print(l1[1:3])

s = slice(1, 3)
print(l1[s])

# zip 拉链函数
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = zip(a, b)
# zip 函数返回一个迭代器，这个迭代器可以被遍历一次
print(tuple(c))

# print(dict(c))

# print(list(c))

# __import__()
# 假设导模块 将模块以字符串的形式导入
x = __import__('time')
x.sleep(3)

