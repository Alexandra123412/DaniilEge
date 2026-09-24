from itertools import product
arr = product('АЕКНТЦ', repeat=5)
count = 0
for i in arr:
    count += 1
    s = ''.join(i)
    if s[0] != 'А' and s[0] != 'Е' and s[0] != 'К':
        if s.count('Т') >= 1:
            if count % 2 == 0:
                print(count)
                break