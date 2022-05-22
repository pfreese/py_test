
def isPalindrome(r):
    rL = len(r)
    rHalf = rL // 2
    for i in range(rHalf):
        if r[i] != r[rL - i - 1]:
            return False
    return True


def longestPalindrome(s):

    sLen = len(s)
    if sLen < 2:
        return s
    if sLen == 2:
        if isPalindrome(s):
            return s
        else:
            return s[0]
    palindromesTs = []
    for l in range(2, 4):
        palindromesTs += [(i, l) for i in range(sLen - l + 1) if isPalindrome(s[i:(i+l)])]
    if len(palindromesTs) == 0:
        return s[0]
    print(palindromesTs)

    def expandIfPossible(T):
        startingIdx = T[0]
        palLen = T[1]
        beforeIdx = startingIdx - 1
        afterIdx = startingIdx + palLen
        if (beforeIdx >= 0) and (afterIdx < sLen) and (s[beforeIdx] == s[afterIdx]):
            return (startingIdx - 1, palLen + 2)
        else:
            return None

    def expandPalindromesTs(pt):
        expanded = [expandIfPossible(T) for T in pt]
        return [e for e in expanded if e is not None]

    def maxPalLen(pt):
        if len(pt) == 0:
            return 0
        return max([T[1] for T in pt])

    expandedPalindromes = expandPalindromesTs(palindromesTs)
    while maxPalLen(expandedPalindromes) > maxPalLen(palindromesTs):
        palindromesTs = expandedPalindromes
        expandedPalindromes = expandPalindromesTs(palindromesTs)
    allPalindromes = palindromesTs + expandedPalindromes
    # Get the max len.
    filtMaxPalLen = [T for T in allPalindromes if T[1] == maxPalLen(allPalindromes)]
    startIdx = filtMaxPalLen[0][0]
    palLen = filtMaxPalLen[0][1]

    return s[startIdx:(startIdx + palLen)]

print(longestPalindrome("aaaa"))
