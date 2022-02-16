"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""


def string_match(a, b):
    quantidade_repeticoes = cont = 0
    quantidade_tamanho_2_a = len(a) - 2

    while True:
        if a[cont:cont+2] in b:
            quantidade_repeticoes += 1
        if cont >= quantidade_tamanho_2_a:
            break

        cont += 1

    return(quantidade_repeticoes)


if __name__ == '__main__':
    assert string_match('xxcaazz', 'xxbaaz') == 3
    assert string_match('abc', 'abc') == 2
    assert string_match('abc', 'axc') == 0
    assert string_match('xxyyzzaabbcc', 'yzbbccxx') == 5
