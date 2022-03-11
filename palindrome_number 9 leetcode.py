"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""


from tkinter import X


def isPalindrome(x):
    if x < 0:
        flag = False
    else:
        teste = str(x)[::-1]
        if int(teste) == x:
            flag = True
        else:
            flag = False

    return flag


if __name__ == '__main__':
    assert isPalindrome(121) == True
    assert isPalindrome(848) == True
    assert isPalindrome(22022022) == True
    assert isPalindrome(259952) == True
    assert isPalindrome(-121) == False
    assert isPalindrome(10) == False
