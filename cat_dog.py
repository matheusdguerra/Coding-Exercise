"""
Retorna True se a string "cat" e "dog" aparecerem o mesmo número de vezes na string fornecida.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""


def catdog(string):
    flag = False
    cont_dog = string.count('dog')
    cont_cat = string.count('cat')

    if cont_dog == cont_cat:
        flag = True

    return flag


if __name__ == '__main__':
    assert catdog('catdog') == True
    assert catdog('catcat') == False
    assert catdog('1cat1cadodog') == True
