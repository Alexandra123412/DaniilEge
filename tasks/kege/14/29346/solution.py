def f(n, a):
    return n + a

def g(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(g(5))

def h(n):
    if n < 0:
        return 'Возраст некорректный'
    elif 0 <= n < 18:
        return 'Несовершеннолетний'
    else:
        return 'Совершеннолетний'
print(h(19))

def k(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(n - 2):
            t = b
            b = a + b
            a = t
        return b
print(k(10))