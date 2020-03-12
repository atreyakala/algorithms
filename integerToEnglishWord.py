BILLION  = 1000000000
MILLION  = 1000000
THOUSAND = 1000
HUNDRED  = 100
TWENTY   = 20
TEN      = 10
TENS         = "Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
LESS_THAN_20 = "One Two Three Four Five Six Seven Eight Nine Ten \
                Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()

def numberToWords(num):
    if num == 0:
        return "Zero"
    segments = []
    baseStrings = (BILLION, "Billion"), (MILLION, "Million"), (THOUSAND, "Thousand"), (HUNDRED, "Hundred")
    for base, string in baseStrings:
        if num >= base:
            segments += [(numberToWords(num / base)), string]
            num %= base
    if num >= TWENTY:
        tenner = TENS[(num / TEN) - 1]
        segments.append(tenner)
        num %= TEN
    if num > 0:
        segments.append(LESS_THAN_20[num - 1])
    return " ".join(segments)
