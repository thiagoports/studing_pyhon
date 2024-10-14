x = int(input())
a = x // 365
x %= 365
m = x // 30
x %= 30
print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{x} dia(s)')
