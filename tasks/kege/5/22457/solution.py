def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n = n // 7
    return s

def q(n):
    n_s = f(n)
    a = n_s.count('1')
    b = n_s.count('2')
    c = n_s.count('3')
    d = n_s.count('4')
    e = n_s.count('5')
    h = n_s.count('6')
    g = a + b * 2 + c * 3 + d * 4 + e * 5 + h * 6
    if g % 2 == 0:
        n_s = n_s + '555'
    else:
        n_s = '33' + n_s + '6'
    return int(n_s, 7)

for i in range(1, 1000):
    r = q(i)
    if r < 12717:
        print(i)