username="chaiaurcode"

def func():
    username="chai"
    print(username)

print(username)

func()

x=99
# def func2(y):
#     z=x+y
#     return z

# print(func2(5))

def func3():
    global x
    x=12

func3()
print(x)

def f1():
    x=88
    def f2():
        print(x)
    return f2
f3=f1()


def chaicode(num):
    def actual(x):
        return x**num
    return actual

chai=chaicode(3)
print(chai)
print(chai(3))


