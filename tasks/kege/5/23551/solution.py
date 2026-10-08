def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s

def q(n):
    n_s = f(n)
    if n % 2 == 0:
        n_s = '10' + n_s
    else:
        n_s = '1' + n_s + '01'
    return int(n_s, 2)

for i in range(1, 1000):
    r = q(i)
    if r < 30:
        print(i)