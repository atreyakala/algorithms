"""
1209. Remove All Adjacent Duplicates in String II https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Constrains:
    1 <= s.length <= 105
    2 <= k <= 104
    s only contains lower case English letters.
"""


def remove_duplicates(string: str, k: int) -> str:
    stack = []

    for char in enumerate(string):
        if stack and stack[-1][0] == char:
            if stack[-1][1] == k - 1:
                stack.pop()
            else:
                stack[-1][1] += 1
        else:
            stack.append([char, 1])

    return "".join(char * count for char, count in stack)

# O(n) | O(n)


def test_0():
    assert remove_duplicates("deeedbbcccbdaa", 3) == "aa"
