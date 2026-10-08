def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s

def q(n):
    n_s = f(n)
    a = n_s.count('1')
    b = n_s.count('2')
    if (a + b * 2) % 9 == 0:
        n_s = n_s + '2'
    else:
        c = f((a + b * 2) % 9)
        n_s = n_s + c
    return int(n_s, 3)

mn = float('inf')
for i in range(167, 1000):
    r = q(i)
    if r < mn:
        mn = r
print(mn)
