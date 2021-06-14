"""
22. Generate Parentheses https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
"""

from typing import List


def generate_parenthesis(n: int):
    result = []
    generate(n, result)
    print(result)
    return result


def generate(n: int, result: List[str] = [], opening_braces_count: int = 0, closing_braces_count: int = 0,
             current: str = "") -> None:
    if len(current) == 2 * n:
        result.append(current)
        return

    if opening_braces_count < n:
        generate(n, result, opening_braces_count + 1, closing_braces_count, current + "(")
    if closing_braces_count < opening_braces_count:
        generate(n, result, opening_braces_count, closing_braces_count + 1, current + ")")


def test_0():
    assert generate_parenthesis(1) == ["()"]


def test_1():
    assert generate_parenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
