def revers(n):
    isNeg = n < 0
    if isNeg:
        n *= -1
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n = n // 10
    if isNeg:
        r*= -1
    return r

print(revers(int(input("число: "))))