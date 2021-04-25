# Leetcode-1047: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can.
# Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

# Input: "abbaca"
# Output: "ca"
# Explanation: For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
# The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

from collections import deque

def removeDuplicates(string: str) -> str:
    charStack = deque()
    for char in string:
        if charStack and charStack[-1] == char:
            charStack.pop()
        else:
            charStack.append(char)
    return "".join(charStack)

from hamcrest import assert_that, equal_to
import unittest

class Test(unittest.TestCase):
    def test_0(self):
        assert_that(removeDuplicates("abbaca"), equal_to("ca"))
    
    def test_1(self):
        assert_that(removeDuplicates("aaa"), equal_to("a"))
    
    def test_2(self):
        assert_that(removeDuplicates("baca"), equal_to("baca"))

if __name__ == '__main__':
    unittest.main()
