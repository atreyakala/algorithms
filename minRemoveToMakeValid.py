def minRemove(string):
    stack = []
    toBeIgnored = set()
    for i, char in enumerate(string):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                toBeIgnored.add(i)
    for i in stack:
        toBeIgnored.add(i)
    result = []
    for i, char in enumerate(string):
        if i not in toBeIgnored:
            result.append(char)
    return "".join(result)
