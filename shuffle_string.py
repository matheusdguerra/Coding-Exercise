"""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.


Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Constraints:

s.length == indices.length == n
1 <= n <= 100
s consists of only lowercase English letters.
0 <= indices[i] < n
All values of indices are unique.
"""


def restoreString(s, indices):
    list_str = []
    list = []

    for char in s:
        list_str.append(char)

    dict_from_list = dict(zip(indices, list_str))

    for idx in range(len(dict_from_list)):
        list.append(dict_from_list[idx])

    return ''.join(list)


if __name__ == '__main__':
    assert restoreString('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]) == 'leetcode'
    assert restoreString('abc', [0, 1, 2]) == 'abc'
