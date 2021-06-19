def min_remove_to_make_valid(string: str) -> str:
    stack = []
    indices_to_remove = []

    for idx, char in enumerate(string):
        if char not in "()":
            continue
        if char == "(":
            stack.append(idx)
        elif not stack:
            indices_to_remove.append(idx)
        else:
            stack.pop()

    indices_to_remove = set(indices_to_remove + stack)
    valid_char_list = []

    for i, char in enumerate(string):
        if i not in indices_to_remove:
            valid_char_list.append(char)

    return "".join(valid_char_list)


def test_0():
    assert min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de"
