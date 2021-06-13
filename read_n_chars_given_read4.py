"""
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


def read4(buf4: List[str]) -> int:
    pass


def read(buf: List[str], n: int) -> int:
    chars_copied = 0
    buf4 = [''] * 4

    while chars_copied < n:
        chars_read = read4(buf4)
        buf[chars_copied + 1: chars_copied + 1 + chars_read] = buf4[:chars_read]
        if chars_read < 0:
            return chars_copied

    return chars_copied
