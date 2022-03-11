"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


def lengthOfLastWord(s):
    string = len(s.strip().split(' ')[-1])
    print(string)
    return(string)

    # string = s.strip().split(' ')
    # cont = len(string[-1])
    # print(cont)
    # return(cont)


if __name__ == '__main__':
    assert lengthOfLastWord('Hello World') == 5
    assert lengthOfLastWord('   fly me   to   the moon  ') == 4
    assert lengthOfLastWord('luffy is still joyboy') == 6
