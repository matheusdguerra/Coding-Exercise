"""
Dados 3 valores int, retorne sua soma.
No entanto, se algum dos valores for um adolescente (13..19)
    -- esse valor contará como 0
    -- exceto que 15 e 16 não contam como adolescentes.

Escreva um auxiliar separado "def fix_teen(n):"que receba um valor int e retorne esse valor fixo para a regra teen.
Desta forma, você evita repetir o código teen 3 vezes (ou seja, "decomposição").
Defina o auxiliar abaixo e no mesmo nível de recuo que o principal no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""


def fix_teen(list):
    lista_teen = []
    for n in list:
        if n >= 13 and n <= 19 and n not in (15, 16):
            n = 0
            lista_teen.append(n)
        else:
            lista_teen.append(n)

    print(lista_teen)
    return(lista_teen)


def no_teen_sum(list):
    return sum(fix_teen(list))


if __name__ == '__main__':
    assert no_teen_sum([1, 2, 3]) == 6
    assert no_teen_sum([2, 13, 1]) == 3
    assert no_teen_sum([2, 1, 14]) == 3
    assert no_teen_sum([2, 1, 16]) == 19
    assert no_teen_sum([15, 1, 13]) == 16
