"""
Temos um papagaio falando alto. 
O parâmetro "hora" é a hora atual no intervalo 0..23. 
Estamos com problemas se o papagaio estiver falando e a hora for antes das 7 ou depois das 20. 
Retorne True se estivermos com problemas.
"""


def papagaio(falando, hora):
    if falando:
        if hora <= 20 and hora >= 7:
            print('1')
            return ('Sem Defeito')
        else:
            print('2')
            return ('Com Defeito')

    else:
        if hora > 20 or hora < 7:
            print('3')
            return ('Sem Defeito')
        else:
            print('4')
            return ('Com Defeito')


if __name__ == '__main__':
    assert papagaio(True, 6) == 'Com Defeito'
    assert papagaio(True, 23) == 'Com Defeito'
    assert papagaio(True, 3) == 'Com Defeito'

    assert papagaio(True, 10) == 'Sem Defeito'
    assert papagaio(True, 19) == 'Sem Defeito'
    assert papagaio(True, 7) == 'Sem Defeito'

    assert papagaio(False, 6) == 'Sem Defeito'
    assert papagaio(False, 23) == 'Sem Defeito'
    assert papagaio(False, 3) == 'Sem Defeito'

    assert papagaio(False, 12) == 'Com Defeito'
    assert papagaio(False, 8) == 'Com Defeito'
    assert papagaio(False, 19) == 'Com Defeito'
