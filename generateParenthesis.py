def generateParenthesis(n):
    out = []
    generate(n, out)
    return out

def generate(n, out, openingBracesCount = 0, closingBracesCount = 0, current = ""):
    if len(current) == 2 * n:
        out.append(current)
        return
    if openingBracesCount < n:
        generate(n, out, openingBracesCount + 1, closingBracesCount, current + "(")
    if closingBracesCount < openingBracesCount:
        generate(n, out, openingBracesCount, closingBracesCount + 1, current + ")")
