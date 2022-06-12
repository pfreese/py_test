
def toRoman(romanStr):
    n = len(romanStr)
    if n == 0:
        return 0
    romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    subtract = 0
    for i in range(n):
        romanVal = romanDict[romanStr[i]]
        if i != (n-1):
            nextRomanVal = romanDict[romanStr[i+1]]
            if nextRomanVal > romanVal:
                total -= romanVal
            else:
                total += romanVal
        else:
            total += romanVal
    return total

assert(toRoman("") == 0)
assert(toRoman("I") == 1)
assert(toRoman("II") == 2)
assert(toRoman("III") == 3)
assert(toRoman("IV") == 4)
assert(toRoman("XIV") == 14)

assert(toRoman("CMLIX") == 959)
assert(toRoman("MDXXIV") == 15244)
