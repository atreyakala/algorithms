"""
227. Basic Calculator II https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7

Input: s = " 3+5 / 2 "
Output: 5

Constraints
    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 231 - 1].
    The answer is guaranteed to fit in a 32-bit integer.
"""


def calculate(string: str) -> int:
    operator_stack = ["+"]
    number_stack = []

    idx = 0
    num = 0

    while idx < len(string):
        char = string[idx]
        if char == " ":
            idx += 1
            continue
        if char.isdigit():
            while idx < len(string) and string[idx].isdigit():
                num = num * 10 + int(string[idx])
                idx += 1
            idx -= 1
            operator = operator_stack.pop()
            if operator == "+":
                number_stack.append(num)
            elif operator == "-":
                number_stack.append(-num)
            elif operator == "*":
                number_stack.append(number_stack.pop() * num)
            else:
                number_stack.append(int(number_stack.pop() / num))
        else:
            operator_stack.append(char)
        num = 0
        idx += 1

    return sum(number_stack)

# O(n) | O(n)


def test_0():
    assert calculate("3+2*2") == 7


def test_1():
    assert calculate(" 3+5 / 2 ") == 5


def test_2():
    assert calculate("420001") == 420001


def test_3():
    assert calculate("2 * 4 * 6") == 48


def test_4():
    assert calculate("42/8 + 5 ") == 10


def test_5():
    assert calculate(" -4/3 + 1 ") == 0


def test_5():
    assert calculate("14 - 3/2") == 13


def test_6():
    assert calculate("  -114 - 1*2") == -116


if __name__ == "__main__":
    test_6()
