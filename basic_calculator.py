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

from typing import Tuple


def calculate(s: str) -> int:
    stack = []
    number = 0
    operator = "+"

    for i, char in enumerate(s):
        if char.isdigit():
            number = number * 10 + int(char)
        if char in "+-*/" or i == len(s) - 1:
            if operator == "+":
                stack.append(number)
            elif operator == "-":
                stack.append(-number)
            elif operator == "*":
                stack.append(stack.pop() * number)
            else:
                stack.append(int(stack.pop() / number))
            number = 0
            operator = char

    return sum(stack)

# O(n) | O(n)


def calculate(s: str) -> int:
    s = s.replace(" ", "")
    stack = []
    result = 0

    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit():
            number, i = get_number(s, i)
            stack.append(number)
        elif char in "+-":
            number, i = get_number(s, i + 1)
            number = number if char == "+" else -number
            stack.append(number)
        else:
            first_operand = stack.pop()
            second_operand, i = get_number(s, i + 1)
            current_result = first_operand * second_operand if char == "*" else int(first_operand / second_operand)
            stack.append(current_result)

    result += sum(stack)
    return result


def get_number(s: str, i: int) -> Tuple[int, int]:
    digits = []
    while i < len(s) and s[i].isdigit():
        digits.append(s[i])
        i += 1

    number = int("".join(digits))
    return number, i


def test_0():
    assert calculate("3+2*2") == 7


def test_1():
    assert calculate(" 3+5 / 2 ") == 5


def test_2():
    assert calculate("420001") == 420001


def test_3():
    assert calculate("42/8 + 5 ") == 10


def test_4():
    assert calculate("2 * 4 * 6") == 48


def test_5():
    assert calculate("14 - 3/2") == 13
