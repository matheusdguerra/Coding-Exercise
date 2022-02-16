"""
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. 
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
- Se o ponto estiver na origem, escreva a mensagem “Origem”.
 -Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.


Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
"""


def ponto(x, y):

    ponto = 'ORIGEM'

    if x > 0 and y > 0:
        ponto = 'Q1'
    elif x < 0 and y > 0:
        ponto = 'Q2'
    elif x < 0 and y < 0:
        ponto = 'Q3'
    elif x > 0 and y < 0:
        ponto = 'Q4'

    return(ponto)


if __name__ == '__main__':
    assert ponto(0.1, 0.1) == 'Q1'
    assert ponto(-4.5, 2.2) == 'Q2'
    assert ponto(-4.5, -2.2) == 'Q3'
    assert ponto(4.5, -2.2) == 'Q4'
    assert ponto(0.0, 0.0) == 'ORIGEM'
