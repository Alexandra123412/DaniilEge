a = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3
def f(n):
    count = 0
    while n > 0:
        if n % 27 == 0:
            count += 1
        n = n // 27
    return count
for x in range(1, 27001):
    n = a - x
    b = f(n)
    if b == 6:
        print(x)
        break