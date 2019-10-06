"""
生成器与迭代器的区别在于，迭代器通常是先定义一个迭代器类，然后通过创建实例来创建迭代器；
而生成器则是先定义一个包含 yield 语句的函数，然后通过调用该函数来创建生成器。
"""
class stringReverse:
    def __init__(self, string):
        self.string = string 
        self.index = len(string)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration("stop")
        self.index -= 1
        return self.string[self.index]

for c in stringReverse("python"):
    print(c)
