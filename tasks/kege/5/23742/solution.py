def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s

def q(n):
    n_s = f(n)
    if n % 3 == 0:
        n_s = n_s + n_s[-3:]
    else:
        a = f(3 *(n % 3))
        n_s = n_s + a
    return int(n_s, 2)

for i in range(1, 1000):
    r = q(i)
    if r >= 200:
        print(i)
        break