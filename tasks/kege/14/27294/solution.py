a = 39 ** 483 + 39 ** 235
def f(n):
    count = 0
    while n > 0:
        if n % 39 == 0:
            count += 1
        n = n // 39
    return count
mx = 0
for x in range(1, 9431):
    n = a - x
    mx = max(f(n), mx)
print(mx)

