"""
Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.

lettersum("") => 0
lettersum("a") => 1
lettersum("z") => 26
lettersum("cab") => 6
lettersum("excellent") => 100
lettersum("microspectrophotometries") => 317
"""


def lettersum(string):
    sum = 0

    # dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    #         'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    #         'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    dict = {chr(97+i): i+1 for i in range(26)}

    for c in string:
        if c in dict.keys():
            sum += int(dict[c])
    print(sum)
    return(sum)


if __name__ == '__main__':
    assert lettersum('') == 0
    assert lettersum('a') == 1
    assert lettersum('z') == 26
    assert lettersum('cab') == 6
    assert lettersum('excellent') == 100
    assert lettersum('microspectrophotometries') == 317
