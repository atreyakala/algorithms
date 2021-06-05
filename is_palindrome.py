
def is_palindrome(string: str) -> bool:
    s = filter(lambda ch: ch.isalnum(), string).lower()
    return all(string[i] == string[~i] for i in range(len(string) // 2))


def test_0():
    assert is_palindrome("aba")


def test_1():
    assert not is_palindrome("abca")


def test_2():
    assert is_palindrome("abba")


# O(n) time | O(1) space
def is_palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

