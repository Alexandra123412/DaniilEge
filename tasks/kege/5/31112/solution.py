def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s

def q(n):
    n_s = f(n)
    if n % 2 == 0:
        n_s = '11' + n_s + '11'
    else:
        n_s = '1' + n_s + '00'
    return int(n_s, 2)

mx = 0
for n in range(1, 1000):
    r = q(n)
    if mx < r <= 113:
        mx = r
print(mx)
