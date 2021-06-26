"""
157. Read N Characters Given Read4 https://leetcode.com/problems/read-n-characters-given-read4/
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from typing import List


def read(buf: List[str], n: int) -> int:
    chars_read_so_far = 0
    while chars_read_so_far < n:
        buf4 = [' '] * 4
        chars_read = read4(buf4)
        if chars_read == 0:
            break
        for i in range(chars_read):
            buf[chars_read_so_far] = buf4[i]
            chars_read_so_far += 1
            if chars_read_so_far == n:
                break
    return chars_read_so_far
