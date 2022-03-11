"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


def addTwoNumbers(l1, l2):
    a = list_to_int(l1)
    b = list_to_int(l2)

    return sum_to_list(a, b)


def list_to_int(list):
    string = ''
    list.reverse()
    for n in list:
        string += str(n)

    return int(string)


def sum_to_list(a, b):
    lista_soma = []
    soma = a + b

    for n in str(soma):
        lista_soma.append(int(n))

    lista_soma.reverse()

    return lista_soma


if __name__ == '__main__':
    assert addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert addTwoNumbers([0], [0]) == [0]
    assert addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
