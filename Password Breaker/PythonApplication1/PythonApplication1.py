import math
numToLetter = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def power(baseNum, powNum):
    result = 1
    for index in range(powNum):
        result = result * baseNum
    return result

def basic(num, digit, base):
    base - 1
    return (int(num/(pow(base, digit)) % base))           # this multiple num * base ^ digit mod base

def NTLF(num):
    digitCount = int(math.log(num, 27))
    result = ""
    if num == 0:
        return "a"
    for index in range(digitCount + 1):
        result = result + numToLetter[0 + basic(num, index, 26)]
    return result

passwordBuffer = ""
tryg = 10000000000000000
while passwordBuffer != "masonah":      
    print(NTLF(tryg), "---", tryg, "---", ((math.log(tryg, 26))+1))
    passwordBuffer = NTLF(tryg)
    tryg += 1 

print("correct")
print("guess:",tryg)
  