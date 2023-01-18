
#  Месяцы
"""year = int(input())

months = {
    "jan": 31,
    "feb": 29 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 28,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 31,
    "oct": 30,
    "nov": 31,
    "dec": 31
}
print(months)"""

# Таблица менделеева
"""
with open("mend.csv") as file:
    txt = file.read()
data = txt.split('\n')[1::]
def parse1(s):
    l = s.split(',')
    if len(s) < 5:
        return
    el = l[2]
    mass = float(l[3])
    num = int(l[0])
    return mass, num
def parse2(s):
    if len(s) < 5:
        return
    l = s.split(',')
    el = l[2]
    mass = float(l[3])
    num = int(l[0])
    return el
data = {parse2(s):parse1(s) for s in data}
print(data)
"""
'''
class Rational:
    def __init__(self, a=None, b=None):
        self.a = a if a != None else 0
        self.b = b if b != None else 1
        b = self.b
        a = self.a
        #print(a,b)
        i=2
        while i <= b:
            if b % i == 0 and a % i == 0:
                b //= i
                a //= i
                i = 1
            i += 1
        self.a=a
        self.b=b
        #print(a, b)

    def __add__(self, other):
        b = self.b * other.b
        a = other.b * self.a + self.b * other.a
        print(f"first: {self.a, self.b} other: {other.a, other.b}")
        print(f"two: {a,b}")
        i=2
        while i <= b:
            if b % i == 0 and a % i == 0:
                b //= i
                a //= i
                i = 1
            i += 1
        return Rational(a, b)
    def __str__(self):
        return f"Rational: [{self.a}] / [{self.b}]" if self.b>1 else f"Rational: [{self.a}]"

R = Rational
x = R(map(int, input().split()))
y = R(map(int, input().split()))
print(x+y)
'''
import psutil
import matplotlib.pyplot as plt

mem=[]
cpu=[]

for i in range(1000):
    n1 =float(psutil.virtual_memory().percent)
    n2 =float(psutil.cpu_percent())
    mem.append(n1)
    cpu.append(int(n2))
plt.subplots(1)
plt.plot(mem)
plt.plot(cpu)
plt.show()
