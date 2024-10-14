A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

PI = 3.14159

TRIANGULO = A * C / 2
CIRCULO = C ** 2 * PI
TRAPEZIO = (A + B) * C / 2
QUADRADO = B ** 2
RETANGULO = A * B

print(f'TRIANGULO: {TRIANGULO:.3f}\nCIRCULO: {CIRCULO:.3f}\nTRAPEZIO: {TRAPEZIO:.3f}\nQUADRADO: {QUADRADO:.3f}\nRETANGULO: {RETANGULO:.3f}')
