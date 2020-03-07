# O(n) time | O(1) space
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -=1
    return True

# O(n) time | O(n) space
def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)
