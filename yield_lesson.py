def sqs(n):
    for i in range(n):
        yield i**2
def factorial(n):
    res = 1
    for i in range(1, n):
        res*=i
    return res
def binom_new(n):
    x = 1
    yield x
    x1 = x
    for k in range(1, n):
        x *= (n - k + 1) / k
        yield int(x)
    yield x1
def palindroms(n):
    for i in range(n):
        s = str(i)
        if s == s[::-1]:
            yield i
def ROMAN_num(x):
    zero = "R"
    r1 = 'I II III IV V VI VII IIX IX'
    r2 = r1.replace("X", "C").replace("V", "L").replace("I", "X")
    r3 = r1.replace("X", "M").replace("V", "D").replace("I", "C")
    r1 = r1.split()
    r2 = r2.split()
    r3 = r3.split()
    r1n = x % 10
    r2n = (x % 100) // 10
    r3n = (x%1000) // 100
    r4n = x // 1000
    res = 'M' * r4n + (r3[r3n-1] if r3n > 0 else '') + (r2[r2n-1] if r2n > 0 else '') + (r1[r1n-1] if r1n > 0 else '')
    return res

def ROMAN_range(n1, n2=None, n3=None):

    if n2 == None:
        for i in range(n1):
            yield ROMAN_num(i)
    elif n3 == None:
        for i in range(n1, n2):
            yield ROMAN_num(i)
    else:
        for i in range(n1, n2, n3):
            yield ROMAN_num(i)

for x in ROMAN_range(1, 100, 7):
    print(x)