def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []
    for i, val in enumerate(values):
        result += (num // val) * numerals[i]
        num %= val
    return "".join(result)

def romanToInt(numeral):
    numeralVal = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    i = 0
    res = 0
    while i < len(numeral):
        lookAhead = numeral[i : i + 2]
        if i + 1 < len(numeral) and lookAhead in numeralVal:
            res += numeralVal[lookAhead]
            i += 2
        else:
            curr = numeral[i]
            res += numeralVal[curr]
            i += 1
    return res
