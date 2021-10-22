def d(x, n, A):
    return x ** n - A

def m(x, n):
    return n * (x ** (n - 1))

def sqrt(n, A):
    x = 1
    kor = abs(d(x, n, A))
    while kor > 1e-5:
        x = x - d(x, n, A)/m(x, n)
        kor = abs(d(x, n, A))
    return x

print(sqrt(int(input("Cтепень корня: ")), int(input("Число: "))))
