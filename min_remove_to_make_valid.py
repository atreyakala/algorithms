"""
1249. Minimum Remove to Make Valid Parentheses https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
    1 <= s.length <= 10^5
    s[i] is one of  '(' , ')' and lowercase English letters.
"""


def min_remove_to_make_valid(string: str) -> str:
    stack = []
    indices_to_remove = []

    for idx, char in enumerate(string):
        if char not in "()":
            continue
        if char == "(":
            stack.append(idx)
        elif not stack:
            indices_to_remove.append(idx)
        else:
            stack.pop()

    indices_to_remove = set(indices_to_remove + stack)
    valid_char_list = []

    for i, char in enumerate(string):
        if i not in indices_to_remove:
            valid_char_list.append(char)

    return "".join(valid_char_list)

# O(n) | O(n)


def test_0():
    assert min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de"
