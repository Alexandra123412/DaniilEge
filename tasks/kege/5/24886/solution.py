def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s

def q(n):
    n_s = f(n)
    if n % 5 == 0:
        n_s = n_s + '11'
    else:
        a = f(n // 5)
        n_s = n_s + a
    return int(n_s, 2)

for i in range(2, 1000, 2):
    r = q(i)
    if r > 896:
        print(i)
        break