"""
A corrida de lesmas é um esporte que cresceu muito nos últimos anos, 
fazendo com que várias pessoas dediquem suas vidas tentando capturar lesmas velozes, 
e treina-las para faturar milhões em corridas pelo mundo. 
Porém a tarefa de capturar lesmas velozes não é uma tarefa muito fácil, 
pois praticamente todas as lesmas são muito lentas. 

Cada lesma é classificada em um nível dependendo de sua velocidade:

Nível 1: Se a velocidade é menor que 10 cm/h .
Nível 2: Se a velocidade é maior ou igual a 10 cm/h e menor que 20 cm/h .
Nível 3: Se a velocidade é maior ou igual a 20 cm/h .

Sua tarefa é identificar qual nível de velocidade da lesma mais veloz de um grupo de lesmas.


Entrada
A entrada consiste de múltiplos casos de teste, e cada um consiste em duas linhas: 
- A primeira linha contém um inteiro L (1 ≤ L ≤ 500) representando o número de lesmas do grupo, 
- A segunda linha contém L inteiros Vi (1 ≤ Vi ≤ 50) representando as velocidades de cada lesma do grupo.

Saída
Para cada caso de teste, imprima uma única linha indicando o nível de velocidade da lesma mais veloz do grupo.
"""


def classificacao(lista_velocidades):
    max_velocidade = max(lista_velocidades)
    classificacao = 2

    if max_velocidade >= 20:
        classificacao = 3
    elif max_velocidade < 10:
        classificacao = 1

    return classificacao


if __name__ == '__main__':
    assert classificacao([10, 10, 10, 10, 15, 18, 20, 15, 11, 10]) == 3
    assert classificacao([1, 5, 2, 9, 5, 5, 8, 4, 4, 3]) == 1
    assert classificacao([19, 9, 1, 4, 5, 8, 6, 1, 1, 9, 7]) == 2
