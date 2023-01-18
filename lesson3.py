import math

"""
class Vec:
    def __init__(self, *coords, name=""):
        self.coords = coords
        self.name = name

    def distance(self, other):
        return math.sqrt(sum([(self.coords[i] - other.coords[i]) ** 2 for i in range(len(self.coords))]))

    def __add__(self, other):
        return Vec(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __mul__(self, other):
        return Vec(*[self.coords[i] * other.coords[i] for i in range(len(self.coords))])

    def __truediv__(self, other):
        return Vec(*[self.coords[i] / other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other):
        return Vec(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __floordiv__(self, other):
        return Vec(*[self.coords[i] // other.coords[i] for i in range(len(self.coords))])

    def __mod__(self, other):
        return Vec(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __str__(self):
        return 'Vector[' + ' : '.join(map(str, self.coords)) + ']'


x = Vec(1, 2, 3)
y = Vec(3, 4, 5)
print(x + y)

"""


class RomNum:
    def __init__(self, num="0"):
        self._rdecode = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))
        self.num = self.convert(num)



    def convert(self, roman):
        result = 0
        for r, r1 in zip(roman, roman[1:]):
            rd, rd1 = self._rdecode[r], self._rdecode[r1]
            result += -rd if rd < rd1 else rd
        return result + self._rdecode[roman[-1]]

    def rom_num(self, x):
        zero = "R"
        r1 = 'I II III IV V VI VII IIX IX'
        r2 = r1.replace("X", "C").replace("V", "L").replace("I", "X")
        r3 = r1.replace("X", "M").replace("V", "D").replace("I", "C")
        r1 = r1.split()
        r2 = r2.split()
        r3 = r3.split()
        r1n = x % 10
        r2n = (x % 100) // 10
        r3n = (x % 1000) // 100
        r4n = x // 1000
        res = 'M' * r4n + (r3[r3n - 1] if r3n > 0 else '') + (r2[r2n - 1] if r2n > 0 else '') + (
            r1[r1n - 1] if r1n > 0 else '') if x > 0 else zero
        return res

    def __add__(self, other):
        return RomNum(self.num + (other.num if type(other) != type(1) else other))

    def __mul__(self, other):
        return RomNum(self.num * (other.num if type(other) != type(1) else other))

    def __truediv__(self, other):
        return RomNum(self.num / (other.num if type(other) != type(1) else other))

    def __sub__(self, other):
        return RomNum(self.num - (other.num if type(other) != type(1) else other))

    def __floordiv__(self, other):
        return RomNum(self.num // (other.num if type(other) != type(1) else other))

    def __mod__(self, other):
        return RomNum(self.num % (other.num if type(other) != type(1) else other))

    def __str__(self):
        return f"Roman Number: [{self.rom_num(self.num)}]"


if __name__ == "__main__":
    a = RomNum("XVI")
    b = RomNum("MLI")
    c = RomNum("MIX")
    print((c + b - a) // 2 + c * a)
