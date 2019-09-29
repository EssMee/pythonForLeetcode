def test(value, step):
    print("test starts")
    current = 0
    for i in range(value):
        current += i * step
        yield current

t = test(10,2)
print("=================")
print(next(t))
print(next(t))
print(next(t))

"""
=================
test starts
0
2
6
从上面的输出结果不难看出，当程序执行 t = test(10, 2) 调用函数时，程序并未开始执行 test() 函数；
当程序第一次调用 next(t) 时，test() 函数才开始执行。
"""
