a = (16 ** 350 * (15 * 3 - 29) ** (4 ** (2 + 5)) + 1007) // 63
def f(n):
    count = 0
    while n > 0:
        if n % 4 == 1:
            count += 1
        n = n // 4
    return count
print(f(a))