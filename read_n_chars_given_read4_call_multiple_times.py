"""
158. Read N Characters Given Read4 II - Call multiple times https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

The read4 API is already defined for you.
def read4(buf4: List[str]) -> int:

Input: file = "abc", queries = [1,2,1]
Output: [1,2,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.

Input: file = "abc", queries = [4,1]
Output: [3,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
"""


from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.queue = deque([])

    def read(self, buf: List[str], n: int) -> int:
        chars_read_so_far = 0
        while chars_read_so_far < n:
            if len(self.queue) > 0:
                buf[chars_read_so_far] = self.queue.popleft()
                chars_read_so_far += 1
            else:
                current_buffer = [' '] * 4
                chars_read = read4(current_buffer)
                if chars_read == 0:
                    break
                for i in range(chars_read):
                    self.queue.append(current_buffer[i])
        return chars_read_so_far
