"""
Leia quatro valores inteiros A, B, C e D. 
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D 
segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA
"""


def diferenca(a, b, c, d):
    dif = (a * b - c * d)
    return (dif)


if __name__ == '__main__':
    assert diferenca(5, 6, 7, 8) == -26
    assert diferenca(0, 0, 7, 8) == -56
    assert diferenca(5, 6, -7, 8) == 86
