a = (25 ** 500 * (4 * 6 + 1) ** (5 ** 4) + 7) // 128
def f(n):
    count = 0
    while n > 0:
        if n % 5 == 4:
            count += 1
        n = n // 5
    return count
print(f(a))