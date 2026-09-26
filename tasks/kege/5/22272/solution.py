def f(n):
    s = ''
    while n > 0:
        s = str(n % 9) + s
        n = n // 9
    return s

def q(n):
    n_s = f(n)
    if n_s[0] == '7':
        n_s = n_s.replace('6', '#')
        n_s = n_s.replace('3', '6')
        n_s = n_s.replace('#', '3')
        n_s = '34' + n_s
    else:
        n_s = '3' + n_s[1:] + '45'
    return int(n_s, 9)

for i in range(1, 1000):
    r = q(i)
    if r < 2876:
        print(i)
