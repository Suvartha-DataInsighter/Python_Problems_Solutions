def gen_fun2():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
z=gen_fun2()
print(next(z))
print(next(z))
print(next(z))
print(next(z))