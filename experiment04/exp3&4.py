import math

def fuhuatixing(func, a, b, n):
    h = (b - a) / float(n)
    xi = [a + k * h for k in range(1,n)]
    xk_sum = sum([func(x) for x in xi])
    result = h / 2 * (1 + 2 * xk_sum + func(b))
    return result

def func(x):
    return math.sin(x) / (x * pow(math.e, x))
a = 0
b = 2
n = 100
print('=======复化梯形公式=======')
print(fuhuatixing(func, a, b, n))
# print('--------------')
print('=======变步长梯形法=======')

def bianbuchangtixing(func, a, b):
    h = b - a
    loss = 1.0
    x = a + 0.5 * h
    T1 = (1 + func(b)) * h / 2
    T2 = T1 / 2 + func(x) / 2
    while abs(T2 - T1) > 1e-5:
        print(T1)
        h = h / 2
        T1 = T2
        sum_xk = 0
        x = a + 0.5 * h
        sum_xk = sum_xk + func(x)
        x = x + h
        while(x < b):
            sum_xk = sum_xk + func(x)
            x = x + h
        T2 = T1 / 2 + 0.5 * h * sum_xk
    print(T2)

bianbuchangtixing(func, a, b)
