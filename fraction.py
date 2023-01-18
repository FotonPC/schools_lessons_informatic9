import math


class Fraction:

    def __init__(self, a=1, b=1, c=0):

        if type(a) == type(str()):
            s, d = map(int, a.split('/'))
            a = s
            b = d

        if type(a) == type(self):
            a = a.a
            b = a.b

        self.a = b * c + a
        self.b = b
        self.nod()

    def nod(self):
        n = math.gcd(self.a, self.b)
        self.a //= n
        self.b //= n

    def __str__(self):
        return f"Fraction: {self.a} / {self.b}"

    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, other.b * self.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - self.b * other.a, other.b * self.b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, other.b * self.b)

    def __truediv__(self, other):
        return Fraction(self.a * other.b, other.a * self.b)

    def __float__(self):
        return float(self.a / self.b)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return float(self) != float(other)


if __name__ == "__main__":
    D = Fraction
    F = Fraction
    Drob = Fraction

    cmd = input(">>> ")
    while cmd != 'exit':

        try:
            exec(cmd)
        except Exception as e:
            print(e)

        cmd = input(">>> ")

    print("Завершено")
