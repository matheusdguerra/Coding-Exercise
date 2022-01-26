"""
Regras FizzBuzz

1. Se a posição for multipla de 3: fizz
2. Se a posição for multipla de 5: buzz
3. Se a posição for multipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição vale o próprio nº

"""
from functools import partial


def multiple_of(base, num): return num % base == 0


multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_5(pos) and multiple_of_3(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'

    return say


# Testes no terminal
# C:\Users\Matheus.Guerra.CETIL\PycharmProjects\fizzbuzz>python fizzbuzz.py -v
# C:\Users\Matheus.Guerra.CETIL\PycharmProjects\fizzbuzz>python -m unittest

# Teste após separar a classe do programa principal
# C:\Users\Matheus.Guerra.CETIL\PycharmProjects\fizzbuzz>python -m unittest

'''
def assert_equal(result_robot, expected):
    from sys import _getframe

    msg = 'Fail: Line {} got {} expecting {}'

    if not result_robot == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result_robot, expected))


if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
'''

"""
Testes no terminal
Chamar python
from fizzbuzz import robot
>>> robot(1)
'1'
>>> robot(3)
'fizz'
>>> robot(5)
'buzz'
>>> robot(15)
'fizzbuzz'
>>> robot(15)

"""
