'''
Testing the use of __dict__
'''
class A(object):
    a=0 #类属性
    def __init__(self):
        self.b=1.0 #实例属性

aa=A()
# 返回类内部所有属性和方法所对应的字典
print(A.__dict__)
# 返回实例属性和值组成的字典
print(aa.__dict__)