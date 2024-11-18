from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        common_divisor = gcd(a, b)
        self.a = a // common_divisor
        self.b = b // common_divisor
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Операнды должны иметь тип Fraction.")
        new_a = (self.a * other.b) + (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Операнды должны иметь тип Fraction.")
        new_a = (self.a * other.b) - (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Операнды должны иметь тип Fraction.")
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Операнды должны иметь тип Fraction.")
        if other.a == 0:
            raise ZeroDivisionError("Нельзя делить на ноль/")
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.a * other.b == other.a * self.b

    def __str__(self):
        if self.b == 1:
            return str(self.a)
        return f"{self.a}/{self.b}"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))