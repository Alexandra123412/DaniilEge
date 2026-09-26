from itertools import product
arr = product('ЕЛНОСЦ', repeat=6)
count = 0
for i in arr:
    count += 1
    s = ''.join(i)
    if s[0] != 'Ц' and s[0] != 'Н':
        if s.count('Ц') == 1 and s.count('Н') == 1:
            if count % 2 != 0:
                print(count)