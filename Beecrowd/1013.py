a, b, s = input().split()

a = int(a)
b = int(b)
s = int(s)

maior = (a + b + abs(a-b)) / 2

if maior > s:
    print(f'{maior} eh o maior ')
else:
    print(f'{s} eh o maior ')