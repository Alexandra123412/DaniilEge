a = 64 ** 678 + 55 ** 123
def f(n):
    count = 0
    while n > 0:
        if n % 25 == 0:
            count += 1
        n = n // 25
    return count
mx = 0
for x in range(1, 232):
    n = a - x
    mx = max(f(n), mx)
print(mx)